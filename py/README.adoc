
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

== Insert from command line

----
./run_insert.py <run_id> <parameters>
----

== Insert from Python

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

The +N1=2,NE=6+ sample looks relevant.  What was its metadata?

----
$ candle_db query run run_id:workflow.swift-276\\:N1=1,NE=5
results: 1
----
date_inserted = 2017-04-19T18:24:37.292Z
benchmark_id  = unknown
experiment_id = workflow.swift-276
parameters    = [u'N1=1,NE=5']
run_id        = workflow.swift-276:N1=1,NE=5
date_modified = 2017-04-19T18:24:37.292Z
----
