# Joern
Data Flow Analysis and Graph Representations

## **Task-1: Data Flow Analysis with Joern CLI**
https://docs.joern.io/quickstart/

**Instructions:** 
Use program1.py for this task. 
Track Data Flow: Using Joern CLI, perform a taint analysis to track the flow of data from the source to the sink. 
Source: The input() method in the provided Python source code. 
Sink: The print() method in the provided Python source code. 

**Procedure:** 
Launch Joern CLI. 
Load the provided Python source code (program1.py) into Joern. 
Execute taint analysis to track data flow. 
Identify and document the path(s) of data-flow from the source to the sink. 
Ensure all steps are executed on the Command Line Interface (CLI) of Joern.

## **Task-2: Data Flow Analysis with Joern interpreter**
https://docs.joern.io/interpreter/

**Instructions:** 
Use program2.py for this task. 
Implementation: Create a Scala-based file to analyze the data flow in the provided Python source code (program2.py). 
Track Data Flow: Without using Joern CLI, implement taint analysis to track the flow of data from the source to the sink. 
Source: The equivalent of the input() method in Scala. 
Sink: The equivalent of the print() method in Scala. 

**Procedure:** 
Write a Scala program that replicates the functionality of the provided Python source code. 
Implement data flow tracking to identify and document the path(s) of data flow from the source to the sink. 
Ensure the analysis is performed without utilizing Joern-cli.

## **Task-3: Exporting Graph Representations with Joern**
https://docs.joern.io/export/

**Instructions:** 
Use program3.py for this task. 
Export Graphs: Utilize Joern's joern-parse and joern-export functionalities to export various graph representations of the provided Python source code. 

**Graph Representations to Export:** 
Abstract Syntax Trees (AST) 
Control Flow Graphs (CFG) 
Control Dependence Graphs (CDG) 
Data Dependence Graphs (DDG) 
Program Dependence Graphs (PDG) 
Code Property Graphs (CPG14) 
Entire graph (Convert to a different graph format - ALL) 

**Procedure:** 
Use joern-parse to parse the source code (program3.py) and create the required graph representations. 
Utilize joern-export to export each of the specified graph representations. 
Ensure all exported graphs are viewable and can be interpreted for understanding the structure and dependencies in the code.
