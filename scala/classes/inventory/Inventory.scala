import scala.collection.mutable.Set;

class Inventory {
	private val product_list = Set[Product]();

	def addProduct(prod: Product) {
		product_list += prod;
	}

	def getValue = {
		var value = 0.0;
		product_list.foreach(prod => value += prod.getPrice * prod.getQuantity);
		value;
	}
}
