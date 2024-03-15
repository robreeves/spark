/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.apache.spark.sql.execution.joins

import scala.collection.mutable
import org.apache.spark.rdd.RDD
import org.apache.spark.sql.catalyst.InternalRow
import org.apache.spark.sql.catalyst.expressions.BindReferences.bindReferences
import org.apache.spark.sql.catalyst.expressions.{Attribute, Expression}
import org.apache.spark.sql.execution.{SparkPlan, UnaryExecNode}

case class JoinKeyStatsExec(child: SparkPlan, keys: Seq[Expression]) extends UnaryExecNode {

  private val keyCounts = new mutable.HashMap[String, Long]()
  private val rowCount = 0L

  override protected def doExecute(): RDD[InternalRow] = {
    val exprs = bindReferences[Expression](keys, child.output)
    child.execute().mapPartitions { iter =>
      iter.map { row =>
        val keyVals = exprs.map(_.eval(row).toString).mkString(",")
        val count = keyCounts.getOrElseUpdate(keyVals, 0) + 1
        keyCounts.put(keyVals, count)

        // TODO check row count and print/write top keys periodically
        logWarning(s"Key: $keyVals, count: $count")

        row
      }
    }
  }

  override def output: Seq[Attribute] = child.output

  override protected def withNewChildInternal(
    newChild: SparkPlan): JoinKeyStatsExec = copy(child = newChild)
}
