// script for accessing local file

function previewFile() {
    const preview = document.querySelector('img');
    const file = document.querySelector('input[type=file]').files[0];
    const reader = new FileReader();
  
    reader.addEventListener("load", function () {
      // convert image file to base64 string
      preview.src = reader.result;
    }, false);
  
    if (file) {
      reader.readAsDataURL(file);
    }
  }

// script for modal //

document.getElementById('imageupload').addEventListener('click', 
function(){
  document.querySelector('.bg-modal').style.display = 'flex';
});

document.querySelector(".close").addEventListener('click', 
function(){
    document.querySelector('.bg-modal').style.display = 'none'
})

