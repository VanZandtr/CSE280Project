
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

  $(document).ready(function () { 
    map = new OpenLayers.Map("map");
    map.addLayer(new OpenLayers.Layer.OSM());
    var fromProjection = new OpenLayers.Projection("EPSG:4326"); 
    var toProjection   = new OpenLayers.Projection("EPSG:900913");
    var position       = new OpenLayers.LonLat(-75.3790, 40.6078).transform( fromProjection, toProjection);
    var zoom           = 18; 
    map.setCenter(position, zoom);
  });


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
    
    $.post("api/path/", 
      { building_start: buildingstart, 
        room_start: roomstart, 
        building_end: buildingdest, 
        room_end: roomdest 
      },
      function(data, status){
        alert("Data: " + data + "\nStatus: " + status);
      });

   /* $.ajax({
      type: "GET",
      url: "api/images/",
      dataType: "json",
      success: function (data) {
          $("body").html("The data is " + JSON.stringify(data));
      }
    });*/

});
  
  
  
