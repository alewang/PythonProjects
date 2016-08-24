object ProductTest {
	def main(args: Array[String]) {
		val test_prod = new Product("test product", 43.51, 100);
		val prod_str = test_prod.getId;
		val prod_price = test_prod.getPrice;
		val prod_qty = test_prod.getQuantity;
		println(prod_str + ' ' + prod_price + ' ' + prod_qty);
	}
}
