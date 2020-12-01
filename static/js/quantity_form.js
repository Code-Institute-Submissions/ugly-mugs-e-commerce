var incrementPlus;
var incrementMinus;

var buttonPlus  = $(".inc");
var buttonMinus = $(".dec");

var incrementPlus = buttonPlus.click(function() {
	var $n = $(this)
	.parent(".col")
	.parent(".qty-box")
	.find(".qty-input");
	$n.val(Number($n.val())+1 );
});

var incrementMinus = buttonMinus.click(function() {
	var $n = $(this)
    .parent(".col")
	.parent(".qty-box")
	.find(".qty-input");
	var amount = Number($n.val());
	if (amount > 0) {
		$n.val(amount-1);
	}
});
