  $(document).ready(function () {
      $('.collapsible').collapsible();
  });

  ClassicEditor
      .create(document.querySelector('#editor'))
      .catch(error => {
          console.error(error);
      });