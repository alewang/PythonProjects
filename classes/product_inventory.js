function Inventory() {
	/*
	productMap will be a map from names of a
	product to the product description
	*/
	this.productMap = {};
	this.addProduct = addProduct;
	this.printInventory = printInventory;
	this.getInventoryValue = getInventoryValue;
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

function printInventory() {
	for(var name in this.productMap) {
		var product = this.productMap[name];
		console.log(name + ' ' + product.price);
	}
}

function getInventoryValue() {
	var sum = 0.0;
	for(var name in this.productMap) {
		var product = this.productMap[name];
		sum += product.price;
	}
	return sum;
}

function Product(name, price) {
	if(name === undefined) {
		name = "";
	}

	if(price === undefined) {
		price = 0.0;
	}
	else {
		price = parseFloat(price);
		if(isNaN(price)) {
			price = 0.0;
		}
	}

	this.name = name;
	this.price = price;
}

function main() {
	var store1 = new Inventory();
	var store2 = new Inventory();

	var p1 = new Product("toothbrush", 52.55);
	var p2 = new Product("toothpaste", 51.40);

	//store1 has more products than store2
	store1.addProduct(p1);
	store1.addProduct(p2);

	store2.addProduct(p2);

	console.log("Store1's inventory:");
	store1.printInventory();
	console.log("Store1's value: " + store1.getInventoryValue());

	console.log("Store2's inventory:");
	store2.printInventory();
	console.log("Store2's value: " + store2.getInventoryValue());
}
