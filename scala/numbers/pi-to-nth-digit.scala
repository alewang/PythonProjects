#!/usr/bin/env scala

def calc(index: Int): Double = {
	val denom_mid: Long = 2 * index + 1;
	val denom_small: Long = denom_mid - 1;
	val denom_big: Long = denom_mid + 1;
	val sign = getSign(index);

	val denominator = denom_small * denom_mid * denom_big;

	return sign * 4.0 / (denominator);
}

def getSign(index: Int): Int = {
	if(index % 2 == 0) {
		return -1;
	} else {
		return 1;
	}
}

val decimals = scala.math.min(Integer.parseInt(args(0)), 15);
val error_limit = scala.math.pow(10, -decimals);

//Initialize terms for the series
var pi_series: Double = 3;
var term_index = 1;
var term = calc(term_index);
var error = scala.math.abs(term);

while(error > error_limit) {
	pi_series += term;

	term_index += 1;
	term = calc(term_index)
	error = scala.math.abs(term);
}

println("With an allowed error of " + error_limit);
println("Pi is approximately " + pi_series);
