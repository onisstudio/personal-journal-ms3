  $(document).ready(function () {
    $('select').formSelect();
    $('.tooltipped').tooltip();
    $('.fixed-action-btn').floatingActionButton();
    $('.sidenav').sidenav();
    $('.modal').modal();

    $(function () {
      $('a.archive_entry').bind('click', function () {
        var entry_id = $(this).data('id');

        $.getJSON('/_archive_entry', {
          entry_id: entry_id,
        }, function (data) {
          $("#entry-" + entry_id).hide("slow");
          M.toast({
            html: 'Entry successfully archived!',
            classes: 'rounded green'
          });
        });
        return false;
      });
    });

    $(function () {
      $('a.unarchive_entry').bind('click', function () {
        var entry_id = $(this).data('id');

        $.getJSON('/_unarchive_entry', {
          entry_id: entry_id,
        }, function (data) {
          $("#entry-" + entry_id).hide("slow");
          M.toast({
            html: 'Entry successfully unarchived!',
            classes: 'rounded green'
          });
        });
        return false;
      });
    });

    $(document).on("click", ".modal-trigger.delete-confirm", function () {

      //get data-id attribute of the clicked element
      var entry_id = $(this).data('id');

      //add data id for the delete button
      $('.modal-footer').find('a.delete_entry').data('id', entry_id);
    });

    $(function () {
      $('a.delete_entry').bind('click', function () {
        var entry_id = $(this).data('id');

        $.getJSON('/_delete_entry', {
          entry_id: entry_id,
        }, function () {
          $('.modal').modal('close');
          $("#entry-" + entry_id).hide("slow");
          M.toast({
            html: 'Entry successfully deleted!',
            classes: 'rounded green'
          });
        });
        return false;
      });
    });

  });