window.addEventListener('HTMLImportsLoaded', function (e) {
    console.log('Loaded import: ');
    loadTemplate($("#switcher :selected").val());
});
var links = []; 
$('#switcher').change(function () {
    console.log('selected ' + $("#switcher :selected").val());
    $('#canvas').empty();
    loadTemplate($("#switcher :selected").val());
});
$('#issue-controls').hide();
$('#canvas').attr('disabled', 'disabled');

$("#right-side").tabs();
$("#right-side").tabs("option", "active", 0);
$("#tab-dresses").click = function () {
    alert('tab-dresses clicked')
};
var tools_filter = {};
const tools_max = 5;
tools = {};

function toolsItem(id, src, alt) {
    var rez = '<div class="tools-item"><img id="' + id + '" src="' +
        src + '" title="' + alt + '"></div>';
    return rez;
}

function updateToolsFilter(tab) {
    console.log('in tab update');
    $('#' + tab).empty();
    var i = 0;
    for (i; i < tools.length; i++) {
        $('#' + tab).append(
            toolsItem(tools[i]._id, "static/pics/" + tools[i].pictures[0], tools[i].description));
        //$('#' + tools[i]._id).one("click", addIssue);//adding by click
//            $('#' + tools[i]._id).draggable(

    }
    $('.tools-item img').draggable(
        {helper: 'clone'});
}

function getDataForTab(tab) {
    tab = tab || 'tab-all';
    var requests = {
        'tab-all': "https%3A//api.mlab.com/api/1/databases/shopeiro/collections/tools%3Fl%3D12%26apiKey%3Dgyxt40ZuBvX0-Zs_ASfIphz87os52wgf",
        'tab-dresses': "https%3A//api.mlab.com/api/1/databases/shopeiro/collections/tools%3Fl%3D12%26q%3D%7B%22typePrefix%22%3A%22%u041F%u043B%u0430%u0442%u044C%u0435%22%7D%26apiKey%3Dgyxt40ZuBvX0-Zs_ASfIphz87os52wgf",
        'tab-shoes': "https%3A//api.mlab.com/api/1/databases/shopeiro/collections/tools%3Fl%3D12%26q%3D%7B%22typePrefix%22%3A%22%u0422%u0443%u0444%u043B%u0438%22%7D%26apiKey%3Dgyxt40ZuBvX0-Zs_ASfIphz87os52wgf",
        'tab-blues': "https%3A//api.mlab.com/api/1/databases/shopeiro/collections/tools%3Fl%3D12%26q%3D%7B%22typePrefix%22%3A%22%u0411%u043B%u0443%u0437%u0430%22%7D%26apiKey%3Dgyxt40ZuBvX0-Zs_ASfIphz87os52wgf",
        'tab-skirts': "https%3A//api.mlab.com/api/1/databases/shopeiro/collections/tools%3Fl%3D12%26q%3D%7B%22typePrefix%22%3A%22%u042E%u0431%u043A%u0430%22%7D%26apiKey%3Dgyxt40ZuBvX0-Zs_ASfIphz87os52wgf",
        'tab-acc': "https%3A//api.mlab.com/api/1/databases/shopeiro/collections/tools%3Fl%3D12%26q%3D%7B%22typePrefix%22%3A%22%u041A%u043E%u0441%u043C%u0435%u0442%u0438%u0447%u043A%u0430%22%7D%26apiKey%3Dgyxt40ZuBvX0-Zs_ASfIphz87os52wgf"
    };
    $.ajax({
        url: unescape(requests[tab]),
        success: function (data) {
            console.log(data);
            tools = data;
            if (tab) {
                var i;
                for (i = 0; i < tools.length; i++) {
                    tools[i].pictures[0] = tools[i].pictures[0].substring(0, tools[i].pictures[0].length - 3) + 'png';
                    //console.log(tools[i].pictures[0])
                }
                updateToolsFilter(tab);
            }

        }
    });
}

getDataForTab('tab-dresses');
getDataForTab('tab-shoes');
getDataForTab('tab-blues');
getDataForTab('tab-skirts');
getDataForTab('tab-acc');

function canvasItem(id, src, alt) {
    var rez = '<img id="' + id + '"class="tools-item" src="' +
        src + '" title="' + alt + '">';
    return rez;
}

function stopMenu() {
    console.log('try to stop slider');
    $('#slider').slider('destroy');
    $('#issue-controls').hide();
}

jQuery.fn.rotate = function (degrees) {
    $(this).css({'transform': 'rotate(' + degrees + 'deg)'});
};
function menuShow() {
    console.log('' + this + ' clicked');
    $('#issue-controls').show();
    var img = this;
    $('#del_issue').click(function () {
        stopMenu();
        img.remove();

    });
    $('#slider-scale').slider({
        slide: function (event, ui) {
            console.log('you changed scale slider to ' + ui.value);
            var currentScale = 100 + 2 * ui.value;
            $(img).attr('style', 'max-height: ' + currentScale + "%;" + 'max-width: ' + currentScale + "%;");

        },
        change: stopMenu
    });
    $('#slider-rotate').slider({
        slide: function (event, ui) {
            console.log('you changed rotate slider to ' + parseInt(ui.value));
            var currentRotate = (0 + ui.value) * 3.8;
            //$(img).attr('style', 'max-height: ' + currentScale + "%;" + 'max-width: ' + currentScale + "%;");
            $(img).rotate(currentRotate);
        },
        change: stopMenu
    });
}

var eventTarget;
function getEventTarget(event) {
    eventTarget = event.target;
//        console.log(eventTarget);
}

function droppedIn(event, ui) {
    console.log('in droppedIn ' + ui.draggable.attr('id'));
    console.log('in droppedIn ' + $(this).attr('class'));
    console.log('in droppedIn ' + $(this).is(":hover"));

//        if (!$(this).is(":hover")) {return}
    if (this !== eventTarget) {
        return
    }
//        $(this).addClass('opacity');
    $(this).empty().addClass('opacity');
    $('<img src="' + ui.draggable.attr('src') + '">').
     bind('click', menuShow).appendTo(this);
    console.log('dropping over');
//        debugger;

//        $(this).attr('src',ui.draggable.attr('src'));
    //$(this).append("<p>ppp<p>");
//        $(this).append(
//                '<img id="' + ui.draggable.attr('id') + '"class="look-item" src="' +
//                ui.draggable.attr('src') + '" title="' + ui.draggable.attr('title') + '">'
//        );
}

function droppenToEmpty(event, ui) {
    console.log('dropped to empty '+(ui.draggable.attr('id')));
    console.log(ui.position);
    console.log(ui.offset.top, ui.offset.left);
    if (!ui.draggable.attr('id')) return;
    var item='<div style="top:'+ (ui.offset.top-90) + 'px; left:'+(ui.offset.left-80) + 'px"><img src=' + ui.draggable.attr('src')+'></div>';
    $(item).appendTo(this).draggable().click(menuShow);
}

function droppenToCollection(event, ui) {
    console.log('dropped to collection '+(ui.draggable.attr('id')));
    var item='<li class="list-item"><img class="list-item-image" src=' + ui.draggable.attr('src')+'></li>';
    $(item).appendTo(this);

}

function addIssue(e) {
    console.log('in addIssue handler');
    var newitem = $(this).clone();
    newitem.appendTo($('#canvas'));
    newitem.draggable();
    newitem.dblclick(dragOrResize);
    //$(this).clone().draggable().appendTo($('#canvas'));
}

function maxpriceChanged() {
    console.log('max price changed to ' + $('#maxprice').val());
    tools_filter = {price: {'$lt': parseInt($('#maxprice').val())}};
    console.log('filter changed to ' + tools_filter.price);
    tools = shopeiro.chain().find(tools_filter).limit(tools_max).data();
    updateToolsFilter();
}
//$('#filter-submit').click(alert('changed'));

var modeDrag = true;
var issuesSelector;

function dragOrResize(e) {
    console.log("issue clicked");
    issuesSelector = $(e.target);
    //issuesSelector.hide();
    //        issuesSelector.draggable('destroy');
    //        issuesSelector.resizable();

    if (modeDrag) {
        console.log('resizableMode - turned on');
        modeDrag = false;
        issuesSelector.draggable('destroy');
        issuesSelector.resizable();
    }
    else {
        console.log('modeDrag - turned on');
        modeDrag = true;
        issuesSelector.resizable('destroy');
        issuesSelector.draggable();
    }
}
$('#top01').one("click", addIssue);
//    $('#canvas').resizable();
//    $('#top02').draggable();
//http://stackoverflow.com/questions/13198131/how-to-save-a-html5-canvas-as-image-on-a-server
$('#screen').click(function () {
    alert("screen");
    html2canvas(document.getElementById("canvas"), {
        onrendered: function (canvas) {
            document.body.appendChild(canvas);
            var dataURL = canvas.toDataURL();
            console.log(dataURL);
            $.post('upload', {img: dataURL});
            //save2server(canvas);
        }
    });
});
