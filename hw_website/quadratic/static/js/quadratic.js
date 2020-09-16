function Rounding(number) {
    return (Math.round(number*100)/100).toString()
}

$(document).ready(function () {
    $("#btn").click(function () {
        var a = $("#a").val();
        var b = $("#b").val();
        var c = $("#c").val();

        var p = -b/(2*a);
        $("#p").text("p = " + Rounding(p));

        var delta = b**2 - 4*a*c;
        $("#delta").text("delta = " + Rounding(delta));

        var q = -delta/(4*a);
        $("#q").text("q = " + Rounding(q));

        if (delta < 0) {
            $("#x0").text("brak rozwiązań rzeczywistych");
        } else if (delta === 0) {
            $("#x0").text("x1 = x2 = " + Rounding(p));
        } else {
            var x1 = (-b-delta**0.5)/(2*a);
            var x2 = (-b+delta**0.5)/(2*a);
            $("#x0").text("x1 = " + Rounding(x1) + " | x2 = " + Rounding(x2));
        }

        aTemp = a
        bTemp = b
        cTemp = c

        if (parseFloat(a) === 1) { aTemp = ""}

        if (delta < 0) {
            $("#product").text("brak rozwiązań rzeczywistych");
        } else if (delta === 0) {
            if (p < 0) {
                var sign1 = "+";
                var p = -p;
            } else {
                var sign1 = "-";
            }
            $("#product").text("y = " + aTemp + "(x"+ sign1 + Rounding(p) + ")\xB2");
        } else {
            if (x1 < 0) {
                var sign1 = "+";
                var x1 = -x1;
            } else {
                var sign1 = "-";
            }
            if (x2 < 0) {
                var sign2 = "+";
                var x2 = -x2;
            } else {
                var sign2 = "-";
            }
            $("#product").text("y = " + aTemp + "(x"+ sign1 + Rounding(x1) + ")(x" + sign2 + Rounding(x2) + ")");
        }

        var addSign = "x + "
        aTemp = a
        bTemp = b
        cTemp = c
        if (parseFloat(a) === 1) { aTemp = ""}
        if (parseFloat(b) === 1) { bTemp = ""}
        if (parseFloat(c) === 0) {
            cTemp = ""
            var addSign = "x"
        }
        $("#formula").text(aTemp + "x\xB2 + " + bTemp + addSign + cTemp + " = 0");
        });
});
