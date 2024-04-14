@main def exec() = {
  importCode(inputPath = "/home/neo/joern/JoernAnalysis/program2.py", projectName = "Task2")
  val source = cpg.call.name("input")
  val destination = cpg.call.name("print")
  println(destination.reachableByFlows(source).p)
}
