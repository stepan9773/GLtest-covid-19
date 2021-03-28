$(document).ready(function () {
    var selectList = document.getElementById("locality-dropdown");
    $.getJSON('http://127.0.0.1:4000/location', function (result) {
        $.each(result, function (key, entry) {

            for (var i = 0; i < entry.length; i++) {
                var option = document.createElement("option");
                option.value = i;
                option.text = entry[i];

                selectList.appendChild(option);
            }
        })
    });
    $("#submit").on('click', function () {
        let country = $("#locality-dropdown").find("option:selected").text()
        console.log(country)
        console.log(`http://127.0.0.1:4000/location/${country}`)
        $.getJSON(`http://127.0.0.1:4000/location/${country}`, function (result) {
            let main_atrebute = ["location","date","total_cases","new_cases","total_deaths","new_deaths"];
            console.log(result);
            var more_info_card = document.getElementById("more-info");
            more_info_card.innerHTML=''
            $.each(result, function (key, entry){
                console.log(entry);
                var universe_key =0
                $.each(entry, function (field, info){
                    $.each(info, function (field, info){
                        universe_key = field
                    })})
                $.each(entry, function (field, info){

                    if(main_atrebute.includes(field)){
                        document.getElementById(field).innerHTML=`${info[universe_key]}`
                    }
                    else {
                        var text = document.createTextNode(`${field.replace('_', ' ')} : ${info[universe_key]}`);
                        var item = document.createElement('p');
                        item.appendChild(text);
                        more_info_card.appendChild(item);
                        console.log(field, info[universe_key]);
                    }
                })
            })
        })
    });
});