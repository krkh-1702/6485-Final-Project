$('#gan').on('change', function() {
   var path = "static/assets/" + this.value + ".jpg";
    $("#gan-test").attr("src", path)
  });
  