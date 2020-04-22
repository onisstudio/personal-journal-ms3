  $(document).ready(function () {
      $('select').formSelect();
      $('.tooltipped').tooltip();
      $('.fixed-action-btn').floatingActionButton();
      $('.sidenav').sidenav();

      $(function() {
        $('a#archive_entry').bind('click', function() {
          var entry_id = $(this).data('id');

          $.getJSON('/_archive_entry', {
            entry_id: entry_id,
          }, function(data) {
            $("#entry-" + entry_id).hide("slow");
            M.toast({html: 'Entry successfully archived!', classes: 'rounded green'});
          });
          return false;
        });
      });

      $(function() {
        $('a#unarchive_entry').bind('click', function() {
          var entry_id = $(this).data('id');

          $.getJSON('/_unarchive_entry', {
            entry_id: entry_id,
          }, function(data) {
            $("#entry-" + entry_id).hide("slow");
            M.toast({html: 'Entry successfully unarchived!', classes: 'rounded green'});
          });
          return false;
        });
      });

  });