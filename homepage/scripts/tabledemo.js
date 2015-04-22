$(function() {

  var container = $('#table_container');

  $('#previous_page_btn').on('click', function() {
    var page = parseInt(container.data('page'))
    console.log(page);
    container.data('page', Math.max(0, page-1));
    container.trigger('table_refresh');
  });

  $('#next_page_btn').on('click', function() {
    var page = parseInt(container.data('page'))
    console.log(page);
    container.data('page', Math.min(12, page+1)); //// how to make the cap?
    container.trigger('table_refresh');
  });

  container.on('table_refresh', function() {
    $.ajax({
      url: '/homepage/tabledemo.get_table/',
      data: {
        table_page: container.data('page'),
      }
    }).success(function(data) {
      container.html(data);
    })

  }).trigger('table_refresh');

});
