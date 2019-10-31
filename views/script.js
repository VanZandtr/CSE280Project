
//SERVER = "https://cse280project.herokuapp.com/"

/*$(document).ready(function () {
    $.ajax({
        type: "GET",
        url: "api/images/",
        dataType: "json",
        success: function (data) {
            $("body").html("The data is " + JSON.stringify(data));
        }
    });
});*/

  //room pa 202 & 262 


  /*
  $(document).ready(function () { 
    map = new OpenLayers.Map("map");
    map.addLayer(new OpenLayers.Layer.OSM());
    var fromProjection = new OpenLayers.Projection("EPSG:4326"); 
    var toProjection   = new OpenLayers.Projection("EPSG:3857");
    var position       = new OpenLayers.LonLat(-75.3790, 40.6078).transform( fromProjection, toProjection);
    var zoom           = 18; 
    map.setCenter(position, zoom);
    */

    $(document).ready(function () {
        var map = new ol.Map({
            target: 'map',
            layers: [
                new ol.layer.Tile({
                    source: new ol.source.OSM()
            })
            ],
            view: new ol.View({
                center: ol.proj.fromLonLat([-75.3790, 40.6078]),
                zoom: 18
            })
      });
    });

   

    //code for overlaying map that didn't work. It should work though
  /*  var inProj = new OpenLayers.Projection("EPSG:3825");
    var outProj = map.getProjectionObject();
    var extent = new OpenLayers.Bounds(0, 0, 528, 288).transform(inProj, outProj);
    var size = new OpenLayers.Size(1125, 558);
    var options = {
                    opacity: 1.0,
                    isBaseLayer: false,
                    numZoomLevels: 20,
                    format: "image/png",
                };
   
    var ourMap = new OpenLayers.Layer.Image('ourmap', 
                    "/api/path?building_start=packard-2&room_start=packard-202&room_end=packard-262", 
                    extent, 
                    new OpenLayers.Size(1125, 558), 
                    options,
                );
            
    map.addLayer(ourMap);


    console.log("here!");

  });*/

/*
  //stops menu from closing when textfield is clicked
  document.querySelector("#roomstart").addEventListener('click', function(e) {e.stopPropagation()});
  document.querySelector("#buildingstart").addEventListener('click', function(e) {e.stopPropagation()});
  document.querySelector("#roomdest").addEventListener('click', function(e) {e.stopPropagation()});
  document.querySelector("#buildingdest").addEventListener('click', function(e) {e.stopPropagation()});

  $("#Go").click(function() {
    
    //get values from textfields
    var buildingstart = $("#buildingstart").val();
    var roomstart = $("#roomstart").val();
    var buildingdest = $("#buildingdest").val();
    var roomdest = $("#roomdest").val();
    
    //print textfields
    console.log(buildingstart);
    console.log(roomstart);
    console.log(buildingdest);
    console.log(roomdest);

    //clear textfields
    $("#buildingstart").val("");
    $("#roomstart").val("");
    $("#buildingdest").val("");
    $("#roomdest").val("");
    
    var data = {
        building_start: buildingstart, 
        room_start: roomstart, 
        //building_end: buildingdest, 
        room_end: roomdest 
    };

    

   // $("#mapoverlay").html("<img width=\"78px\" src = /api/path?building_start=" + buildingstart + "&room_start=" + roomstart + "&room_end=" + roomdest + ">"); 
    //$("#mapoverlay").html("<img width=\"78px\" src = https://cse280project.herokuapp.com/image/2961b60d28a39e7969eace5fa14abff8.png");
   // $("#mapoverlay").show();

   // "/api/path?building_start=" + buildingstart + "&room_start=" + roomstart + "&room_end=" + roomdest, 

    $.ajax({
        type: 'GET',
        url: '/api/path',
        data: data,
        success: function (data) {   
            $("#overlay").show();
            console.log("Successful!");
            console.log(data);
        }
    });

   */
});
  

