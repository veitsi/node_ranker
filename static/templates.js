var templates = {
    '_empty':{
        items:0
    },
    '_collection':{
        items:0
    },
    'c11': {
        items: 2
    },
    'hearts': {
        items: 5
    },
    'elegant': {
        items: 6
    },
    'styled': {
        items: 7
    },
    'bookmarks': {
        items: 4
    },
    'friday': {
        items: 8
    },
    'ink': {
        items: 5
    },
    'pattern': {
        items: 6
    }
};
function loadTemplate(id) {
    console.log('in template id='+id);
    document.querySelector('#canvas')
        .appendChild(document.importNode(
            document.querySelector('link[rel="import"]').import.querySelector('#' + id).content, true));
    // var i = 1;
    for (var i = 1; i <= templates[id].items; i++) {
        console.log("#" + i);
        $(".item-"+i).droppable({
            drop: droppedIn,
            hoverClass: 'dropHover',
            tolerance: 'pointer'
        });
        $('.item-' + i).bind('mouseenter', getEventTarget); //Добавляем обработчик событий

        //$("#" + i).attr('src', links[i]);
        //$("#" + i).droppable({drop: droppedIn});
    }
    console.log('before collection check');
    if (id==='_collection'){
        console.log('bind on collection dropping');
        $('#collection-template').droppable({
            drop:droppenToCollection
        });
    }

    if (id==='_empty'){
        console.log('bind on empty dropping');
        $('#empty-template').droppable({
            drop:droppenToEmpty
        });
    }

    

}


//        var link = document.querySelector('link[rel="import"]');
//        var template = document.querySelector('link[rel="import"]').import.querySelector('#ink');
//        var clone = document.importNode(template.content, true);

