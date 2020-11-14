function getTop100verbsFor(lang) {
    console.log(lang);
    $.ajax({
        url: "/lang/" + lang + "/top100",
        type: "GET"
    }).done(function (data) {
        verb_list = $('#verb_list');
        verb_list.html('');
        left_column = $("<div></div>");
        right_column = $("<div></div>");
        data.forEach(function (item, i, arr) {
            link = $("<A>" + item + "</A>").attr('href', '#').addClass("list_navy");
            list_item = $("<LI></LI>");
            list_item.append(link)
            link.click(function () {
                $('input#infinitive').val(item).change();
                return false;
            });
            if (i < 50) left_column.append(list_item);
            else right_column.append(list_item);
        })
        verb_list.append(left_column);
        verb_list.append(right_column);
    });
}