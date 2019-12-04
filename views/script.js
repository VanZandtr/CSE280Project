
    $(document).ready(function () {
        var map = new ol.Map({
            interactions: ol.interaction.defaults({mouseWheelZoom:false}),
            target: 'map',
            layers: [
                new ol.layer.Tile({
                    source: new ol.source.OSM()
            })
            ],
            view: new ol.View({
                center: ol.proj.fromLonLat([-75.3790, 40.6078]),
                zoom: 19
            })
      });
    });

    $("#showMaps").click(function() {

	$("#pathMap").hide();
        $("#mapoverlay1").show();
        $("#mapoverlay2").show();
        $("#mapoverlaybtns").show();

        $("#actualmap1").html("");
        $("#actualmap2").html("");
        $("#btnflr2").html("");
        $("#btnflr3").html("");
        $("#btnflr4").html("");

        $("#actualmap1").append('<img id="packard24" src="https://cse280project.herokuapp.com/image/3f135059027fea61200372cbf2cc1970.png"/>');
        $("#actualmap2").append('<img id="packard3" src="https://cse280project.herokuapp.com/image/a23bd24fb1be137d9e92d719966860d8.png"/>');

        $("#btnflr2").append('<button id="floor2" class="mdl-button mdl-js-button mdl-button--fab mdl-js-ripple-effect mdl-button--colored"> 2 </button>');

        $("#btnflr3").append('<button id="floor3" class="mdl-button mdl-js-button mdl-button--fab mdl-js-ripple-effect mdl-button--colored"> 3 </button>');

        $("#btnflr4").append('<button id="floor4" class="mdl-button mdl-js-button mdl-button--fab mdl-js-ripple-effect mdl-button--colored"> 4 </button>');

        $("#btnflr2").click(function() {
            $("#mapoverlay2").hide();
            $("#mapoverlay1").show();
        });

        $("#btnflr3").click(function() {
            $("#mapoverlay2").show();
            $("#mapoverlay1").hide();
        });

        $("#btnflr4").click(function() {
            $("#mapoverlay2").hide();
            $("#mapoverlay1").show();
        });
    });


  //stops menu from closing when textfield is clicked
  document.querySelector("#roomstart").addEventListener('click', function(e){e.stopPropagation()});
  document.querySelector("#roomdest").addEventListener('click', function(e){e.stopPropagation()});

 $("#Go").click(function() {
    //get values from textfields
    var roomstart = $("#roomstart").val();
    var roomdest = $("#roomdest").val();

    //print textfields
    console.log(roomstart);
    console.log(roomdest);

    //clear textfields
    $("#roomstart").val("");
    $("#roomdest").val("");

    $("#pathMap").show();
    $("#pathMap").html("")


    $("#mapoverlay1").hide();
    $("#mapoverlay2").hide();
    $("#mapoverlaybtns").hide();
    $("#pathMap").html("<img id=\"pathpng\" width=\"300px\" src = /path/" + roomstart + "/" + roomdest + ">"); 
    $("#pathMap").show();

});


