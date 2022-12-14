**Updated 5th Nov 2022 see Releases section below**

# buildlogseqtestgraph
Builds a test logseq graph with generated data and query testing capabilities including
 - random pages and blocks, journals, tasks, page tags, block tags, page properties, block properties and links
 - advanced query examples 
 - embedded iframe which uses the online advanced query builder tool https://adxsoft.github.io/logseqadvancedquerybuilder
   - see _https://github.com/adxsoft/logseqadvancedquerybuilder_
   
# Generated Graph
LogseqTestGraph.zip contains a fully generated Test Graph built using _builtlogseqtestgraph.py_

# Usage
`python3 builtlogseqtestgraph.py`


# Before you run buildlogseqtestgraph.py
At a minimum you will need to change the _targetfolder_ address in _builtlogseqtestgraph.py_ so that the builder knows where to build the generated graph


# Advanced Customisation
Assuming you are comfortable with python, modify the generator settings in _builtlogseqtestgraph.py_ as follows

- **targetfolder** - the folder location where the graph is to be built 

- in **PageGroupsToGenerate** array add the following entry and change the values (not the keys) to your page generation requirements

  - `{
        'title': 'Test Pages',
        'pageprefix': 'testpage',
        'nopages': 20,
        'namespace': '',
    },`

- in **JournalsToGenerate** array change the one and only entry to your date range, number of journals to build and the maximum gap in days that can occur

  - `{
    'fromdate': '2020_01_01',
    'todate': '2023_12_31',
    'nojournals': 50,
    'maxincrementindays': 45,
}`
 
# Releases
_Version 0.1_
- original release
_Version 0.2_
- bug fixes and compatibility with _https://github.com/adxsoft/logseqadvancedquerybuilder_ v0.2
- added more page properties adn additional query examples using and and or with command arguments
