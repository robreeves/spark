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

package org.apache.spark.sql

import org.apache.spark.sql.catalyst.expressions.{Attribute, Expression}
import org.apache.spark.sql.catalyst.planning.ExtractEquiJoinKeys
import org.apache.spark.sql.catalyst.plans.logical.{LogicalPlan, UnaryNode}
import org.apache.spark.sql.catalyst.rules.Rule
import org.apache.spark.sql.classic.ColumnConversions.toRichColumn

package object debug {
  case class InlineApproxCount(child: LogicalPlan, columns: Seq[Expression])
    extends UnaryNode {

    override def output: Seq[Attribute] = child.output

    override protected def withNewChildInternal(
      newChild: LogicalPlan): InlineApproxCount = copy(child = newChild)
  }

  object InlineApproxCountInference extends Rule[LogicalPlan] {
    override def apply(plan: LogicalPlan): LogicalPlan = {
      plan.transformUp {
        case j @ ExtractEquiJoinKeys(_, leftKeys, rightKeys, _, _, _, _, _) =>
          val left = wrapJoinInput(j.left, leftKeys)
          val right = wrapJoinInput(j.right, rightKeys)

          j.withNewChildren(Seq(left, right))
      }
    }

    private def wrapJoinInput(
      plan: LogicalPlan,
      sampleKeys: Seq[Expression]) = plan match {
        // TODO do we need this case? It means a user explicitly added it
        // case d: InlineApproxCount => d
        case _ => InlineApproxCount(plan, sampleKeys)
    }
  }

  implicit class Debug(query: Dataset[_]) {
    def inlineApproxCount(columns: Column*): Dataset[_] = {
      val plan = InlineApproxCount(query.logicalPlan, columns.map { _.expr })
      Dataset.ofRows(query.sparkSession, plan)
    }
  }
}
