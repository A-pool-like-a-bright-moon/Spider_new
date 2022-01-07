function zhongbaojinianbao(pageindex) {
var pageindex = pageindex;
var pagesize = 1000;
var isRelationChild = 0;
var relationid = $("#year dd a.on").attr("data-id");
var pagecmd = "zhongbaojinianbao";
var condition = '[{"condition":[{"field":"relationid","value":"' + relationid + '","symbol":"=","isRelationChild":' + isRelationChild + '}],"condition_type":1,"pagesize":' + pagesize + ',"pageindex":' + pageindex + '}]';
var attrArgs = "cmd|search|pagecmd|search|condition";
//为了转换数组与json中的逗号冲突，此处用|search|分隔
var valArgs = "getConditionResult" + "|search|" + pagecmd + "|search|" + condition;
var data = "attrArgs=" + encryption(attrArgs) + "&valArgs=" + encryption(valArgs) + "";
ajaxPublicSearch(data,
function(msg) {
    var obj = eval('(' + msg + ')');
    var HtmlList = '';
    if (obj.data != null) {
        for (var i = 0; i < obj.data.length; i++) {
            //HtmlList += '<li><dl class="ratio-img" data-ratio="0.66029"><dt><img onerror="lod(this)" src="' + obj.data[i]['thumb'] + '"></dt><dd><div class="report_time"><span class="fnt_36">' + obj.data[i]['month'] + '</span><p><i>/</i>' + obj.data[i]['year'] + '</p></div><div class="report_p fnt_16"><p><a href="' + obj.data[i]['file4'] + '" target="_blank">' + obj.data[i]['title'] + '</a></p><p><a href="' + obj.data[i]['file3'] + '" target="_blank">' + obj.data[i]['subtitle'] + '</a></a></p></div></dd></dl></li>';
            HtmlList += '<li>';
            HtmlList += '<dl class="ratio-img" data-ratio="0.66029">';
            HtmlList += '<dt><img onerror="lod(this)" src="' + obj.data[i]['thumb'] + '"></dt>';
            HtmlList += '<dd>';
            HtmlList += '   <div class="report_time">';
            HtmlList += '       <span class="fnt_36">' + obj.data[i]['month'] + '</span>';
            HtmlList += '       <p><i>/</i>' + obj.data[i]['year'] + '</p>';
            HtmlList += '   </div>';
            HtmlList += '   <div class="report_p fnt_16">';
            if (obj.data[i]['file4'] != '' && obj.data[i]['file4'] != 'undefined' && obj.data[i]['file4'] != undefined) {
                HtmlList += '       <p><a href="' + obj.data[i]['file4'] + '" target="_blank">' + obj.data[i]['title'] + '</a></p>';
            }
            if (obj.data[i]['file3'] != '' && obj.data[i]['file3'] != 'undefined' && obj.data[i]['file3'] != undefined) {
                HtmlList += '       <p><a href="' + obj.data[i]['file3'] + '" target="_blank">' + obj.data[i]['subtitle'] + '</a></p>';
            }
            if (obj.data[i]['file'] != '' && obj.data[i]['file'] != 'undefined' && obj.data[i]['file'] != undefined) {
                HtmlList += '       <p><a href="' + obj.data[i]['file'] + '" target="_blank">' + obj.data[i]['text3'] + '</a></p>';
            }
            HtmlList += '   </div>';
            HtmlList += '</dd>';
            HtmlList += '</dl>';
            HtmlList += '</li>';
        }
        var title = $("#year dd a.on").attr("data-val");
        $("#contentTitle").html(title);
    } else {
        HtmlList = '<li>抱歉，没有找到相关信�?/li>';
    }
    console.log(obj.data);
    $("#PublicSearch_Html").html(HtmlList);

});
}