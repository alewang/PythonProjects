object InventoryTest {
	def main(args: Array[String]) {
		val inv = new Inventory;
		val p = new Product("Bacon", 10, 500);
		val bread = new Product("Bread", 2, 1000);
		inv.addProduct(p);
		inv.addProduct(bread);

		println("Total value is " + inv.getValue);
	}
}
