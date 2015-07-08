function Inventory() {
	/*
	productMap will be a map from names of a
	product to the product description
	*/
	this.productMap = {};
	this.addProduct = addProduct;
	this.printInventory = function() {
		for(var name in this.productMap) {
			alert(name);
		}
	}
}

function addProduct() {
	var argIndex;
	for(argIndex = 0; argIndex < arguments.length; argIndex++) {
		var theProduct = arguments[argIndex];
		var pName = theProduct.name;
		if(pName !== undefined && pName !== null) {
			this.productMap[pName] = theProduct;
		}
	}
}

function Product(name) {
	this.name = name;
}

function main() {
	var store1 = new Inventory();
	var store2 = new Inventory();

	var p1 = new Product("toothbrush");
	var p2 = new Product("toothpaste");
	store1.addProduct(p1);
	store2.addProduct(p2);

	alert("Store1's inventory coming up");
	store1.printInventory();
	alert("Store1 complete");

	alert("Store2's inventory coming up");
	store2.printInventory();
	alert("Store2 complete");
}
