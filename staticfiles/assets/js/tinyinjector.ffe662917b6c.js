// We gonna inject that script in admin post template

var script = document.createElement('script');
script.src = 'https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js'
"https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js"
script.type = 'text/javascript'
"text/javascript"
document.head.appendChild(script)
// The output you would get 
// <script src="https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js" type="text/javascript"></script>

//onload so that this will run only when above gets loaded. Reason is it is not working before
// because below stuff load before the above :D
script.onload = function(){
    tinymce.init({
        selector: '#id_content', // changing that id into model's text area's id .
        height : 450,
        plugins: [
        'advlist autolink link image lists charmap print preview hr anchor pagebreak spellchecker',
        'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking',
        'table emoticons template paste help'
        ],
        toolbar: 'undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | ' +
        'bullist numlist outdent indent | link image | print preview media fullpage | ' +
        'forecolor backcolor emoticons | help',
        menu: {
        favs: {title: 'My Favorites', items: 'code visualaid | searchreplace | spellchecker | emoticons'}
        },
        menubar: 'favs file edit view insert format tools table help',
        content_css: 'css/content.css'
    });
}
