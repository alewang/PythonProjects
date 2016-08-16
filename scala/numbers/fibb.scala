#!/usr/bin/env scala
val maximum_index = 100;

def getNthTerm(index: Int): Int = {
	if(index == 0) {
		return 0;
	}

	if(index == 1) {
		return 1;
	}

	return getNthTerm(index - 1) + getNthTerm(index - 2);
}

def main(args: Array[String]) {
	if(args.length < 1) {
		Console.err.println("Not enough arguments");
		return;
	}

	val index = scala.math.min(Integer.parseInt(args(0)), maximum_index);
	val term = getNthTerm(index);
	println("The value of the term at index " + index + " of the Fibbonacci sequence is\n" +
		term);
}

main(args)
