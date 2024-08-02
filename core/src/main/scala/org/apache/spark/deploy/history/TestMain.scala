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

package org.apache.spark.deploy.history

import org.apache.commons.io.FileUtils
import org.apache.spark.SparkConf
import org.apache.spark.internal.config.History.{HISTORY_LOG_DIR, HYBRID_STORE_DISK_BACKEND, HYBRID_STORE_ENABLED, LOCAL_STORE_DIR}

import java.io.File

object TestMain extends App {
  val historyLogDir = args(0)
  val localStoreDir = args(1)
  val appId = args(2)

  FileUtils.deleteDirectory(new File(localStoreDir))

  val conf = new SparkConf()
  conf.set(HISTORY_LOG_DIR, historyLogDir)
  conf.set(LOCAL_STORE_DIR, localStoreDir)
  conf.set(HYBRID_STORE_DISK_BACKEND, "LEVELDB")
  conf.set(HYBRID_STORE_ENABLED, false)

  val provider = new FsHistoryProvider(conf)
  provider.checkForLogs()

  // checkForLogs is async so wait for it to finish
  var ui: Option[LoadedAppUI] = Option.empty
  var count = 0
  var processingTimeSec = 0L
  while (ui.isEmpty && count < 5) {
    count += 1
    val start = System.nanoTime()
    ui = provider.getAppUI(appId, Some("1"))
    processingTimeSec = (System.nanoTime() - start) / 1000000000
    println("sleep")
    Thread.sleep(5000)
  }

  println(ui.map(x => processingTimeSec).getOrElse(-1))
}
