var SERVER = "https://cse280project.herokuapp.com"

$(document).ready(function () {
    $.ajax({
        type: "GET",
        url: SERVER + "/api/images",
        dataType: "json",
        success: function (data) {
            $("body").html("The data is " + JSON.stringify(data));
        }
    });
});

  
  function menuDropdown() {
    $("myMenu").classList.toggle("show");
  }

  window.onclick = function(event) {
    if (!event.target.matches('.menubtn')) {
      var dropdowns = document.getElementsByClassName("menu-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }
  
  map = new OpenLayers.Map("map");
  map.addLayer(new OpenLayers.Layer.OSM());
  var fromProjection = new OpenLayers.Projection("EPSG:4326"); 
  var toProjection   = new OpenLayers.Projection("EPSG:900913");
  var position       = new OpenLayers.LonLat(-75.3783, 40.6069).transform( fromProjection, toProjection);
  var zoom           = 18; 
  map.setCenter(position, zoom);


  
