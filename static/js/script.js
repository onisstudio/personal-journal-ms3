  $(document).ready(function () {
      InlineEditor
          .create(document.querySelector('#editor'), {
              toolbar: {
                  items: [
                      'bold',
                      'italic',
                      'link',
                      'bulletedList',
                      'numberedList',
                      '|',
                      'indent',
                      'outdent',
                      '|',
                      'undo',
                      'redo'
                  ]
              },
              placeholder: 'Type the content here!'
          })
          .catch(error => {
              console.error(error);
          });
  });