$(document).ready(function () {
    // Card Multi Select
    $('input[type=checkbox]').click(function () {
      if ($(this).parent().hasClass('active')) {
        $(this).parent().removeClass('active');
      }
      else
      { $(this).parent().addClass('active'); }
    });
  });




  // Material Select Initialization
$(document).ready(function() {
  $('.mdb-select').materialSelect();
  });






  /* JS for demo only */
var colors = ['1abc9c', '2c3e50', '2980b9', '7f8c8d', 'f1c40f', 'd35400', '27ae60'];

colors.each(function (color) {
  $$('.color-picker')[0].insert(
    '<div class="square" style="background: #' + color + '"></div>'
  );
});

$$('.color-picker')[0].on('click', '.square', function(event, square) {
  background = square.getStyle('background');
  $$('.custom-dropdown select').each(function (dropdown) {
    dropdown.setStyle({'background' : background});
  });
});

/*
 * Original version at
 * http://red-team-design.com/making-html-dropdowns-not-suck
 */