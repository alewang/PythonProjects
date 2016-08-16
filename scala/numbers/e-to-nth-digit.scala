#!/usr/bin/env scala

def calculateE(error_limit: Double): Double = {
	var e = 0.0;
	var index = 0;
	var error = getNthTermOfSeries(index);
	while(error > error_limit) {
		e += error;
		index += 1;
		error = getNthTermOfSeries(index);
	}
	return e;
}

def getNthTermOfSeries(n: Int): Double = {
	val term = 1.0 / factorial(n);
	return term.doubleValue();
}

def factorial(n: Int): Long = {
	if(n == 1 || n == 0) {
		return 1;
	}
	return factorial(n - 1) * n;
}

def main(args: Array[String]): Unit = {
	if(args.length < 1) {
		Console.err.println("Not enough arguments");
		return;
	}
	var decimals = 0;
	try {
		decimals = scala.math.min(Integer.parseInt(args(0)), 15);
	} catch {
		case ex: NumberFormatException => {
			Console.err.println("Unable to parse given argument");
			return;
		}
	}

	if(decimals <= 0) {
		Console.err.println("The number of decimals must be positive");
		return;
	}

	val error_limit = scala.math.pow(10, -decimals);
	val e = calculateE(error_limit);
	println("The value of e is " + e);
}

main(args);
