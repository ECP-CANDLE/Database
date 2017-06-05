
= Database

== Setup

1. Download Solr TGZ:
----
wget http://archive.apache.org/dist/lucene/solr/6.5.0/solr-6.5.0.tgz
tar xfz solr-6.5.0.tgz
----

2. Add .../solr-6.5.0/bin to PATH

3. Checkout the Database schemas
----
git clone git@github.com:ECP-CANDLE/Database.git
----

4. Start solr as yourself with these schemas
You can specify solr home directory by using -Dsolr.solr.home param
----
./bin/solr start -Dsolr.solr.home=.../Database
----
All data is stored in .../Database

5. Start inserting data with the examples in Database/examples

== Basic operation reference

=== Command line tools

* A +curl+-based insertion is [here](https://github.com/ECP-CANDLE/Database/blob/master/examples/run-insert.sh)
* A +wget+-based query is [here](https://github.com/ECP-CANDLE/Database/blob/master/examples/run-query.sh)

=== Python

We are using https://pypi.python.org/pypi/pysolr/3.4.0[pysolr] to access the database from workflows.

==== Setup

. Download:
----
wget https://pypi.python.org/packages/47/d6/91dd269b4443c77905ac5f347318435bfeaa2825ce2763d936e0945f29e4/pysolr-3.6.0.tar.gz
----
. Untar:
----
tar xfz pysolr-3.6.0.tar.gz
----
. Set +PYTHONPATH+ to point to that directory.  You only need +pysolr.py+, you can delete everything else.

* A sample insertion is [here](https://github.com/ECP-CANDLE/Database/blob/master/examples/run-insert-py.sh)
* A sample query is ...
* Our WIP pysolr abstraction is https://github.com/ECP-CANDLE/Database/blob/master/py/run_insert.py[run_insert.py]
https://github.com/ECP-CANDLE/Database/tree/master/py[README]

== Workflow access

== Setup

1. Install pip

2. Do +pip install requests+

3. Download PySolr:
+
----
wget https://pypi.python.org/packages/47/d6/91dd269b4443c77905ac5f347318435bfeaa2825ce2763d936e0945f29e4/pysolr-3.6.0.tar.gz
----

4. Untar it

5. Set +PYTHONPATH+ to include the directory +pysolr-3.6.0+ or copy +pysolr.py+ into +PYTHONPATH+ somewhere

== The CANDLE DB tool

The tool is called +candle_db+.  It contains a nice Python API for accessing the CANDLE Solr database.  It can also be used on the command line.

== Insert from command line

----
./candle_db update run run_id=<run_id> parameters=<parameters> <other key/values...>
----

== Insert from Python

Cf. The SwiftExamples https://github.com/CODARcode/SwiftExamples/blob/5f5ff606afa5a56686def061deea2d75a51dede2/SimpleSweepPyDB/sweep.py=L57[sweep.py], which is called from Swift

----
import candle_db
candle_db.run_insert(run_id=run_id,
                     parameters=params_string,
                     experiment_id=sweep_experiment_id)
----

== Sample transcript after workflows

What have I run so far?

----
$ candle_db ls -c experiment
workflow.swift-276
workflow.swift-279
----

I ran two workflows.  The second looks familiar.  What is its full metadata?

----
$ candle_db query experiment experiment_id:workflow.swift-276
results: 1
date_inserted    = 2017-04-19T18:24:37.033Z
benchmark_id     = unknown
experiment_id    = workflow.swift-276
date_modified    = 2017-04-19T18:24:37.033Z
experiment_title = untitled
----

Ok, what samples did it perform?

----
$ candle_db ls run experiment_id:workflow.swift-276
results: 4
workflow.swift-276:N1=1,NE=6 = N1=1,NE=6
workflow.swift-276:N1=1,NE=5 = N1=1,NE=5
workflow.swift-276:N1=2,NE=6 = N1=2,NE=6
workflow.swift-276:N1=2,NE=5 = N1=2,NE=5
----

The +N1=1,NE=5+ sample looks relevant.  What was its metadata?

----
$ candle_db query run run_id:workflow.swift-276\\:N1=1,NE=5
results: 1
date_inserted = 2017-04-19T18:24:37.292Z
benchmark_id  = unknown
experiment_id = workflow.swift-276
parameters    = [u'N1=1,NE=5']
run_id        = workflow.swift-276:N1=1,NE=5
date_modified = 2017-04-19T18:24:37.292Z
----
