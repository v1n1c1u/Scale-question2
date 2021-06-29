document.addEventListener('DOMContentLoaded', async function () {
    var api = await get_api();
    go(api);
});

async function get_api() {
    /*
     * em app/views.py h� uma fun��o chamada 'api' que retorna um JSON 
     * baseado na api de 'https://www.amock.io/api/fcmaia/countries'.
     * Fiz assim porque a chave 'name' da api do link acima n�o est�
     * entre aspas como uma chave JSON deveria estar
     */
    var response = await fetch('/api', { method: 'GET' });
    var json = await response.json();
    return json;
}

async function go(api) {
    /*
     * Mapeia o n�mero de fronteiras em uma lista de pa�ses com esse n�mero de fronteiras
     */ 
    let map = new Map();
    for (var country in api) {
        var numOfFrontiers = api[country].fronteiras.length;
        if (!map.has(numOfFrontiers)) {
            map.set(numOfFrontiers, []);
        }
        map.get(numOfFrontiers).push(api[country].name);
    }
    //Faz um array do n�mero de fronteiras e ordena de forma decrescente
    var keyset = Array.from(map.keys());
    keyset.sort(function (a, b) { return b - a });

    var div_to_append = document.querySelector("#list");

    var position = 1; //posi��o dos pa�ses no ranking de pa�ses com mais fronteiras

    //varre a lista ordenada de chaves
    for (var key in keyset) {
        var countries = map.get(keyset[key]);
        var output = `${position} - `;

        var countries_number = countries.length;

        //para cada pa�s com o n�mero de fronteiras igual a keyset[key]
        for (var country in countries) {
            if (countries_number == 1) {
                          // [nome do pa�s] ([n�mero de fronteiras])
                output += `${countries[country]} (${keyset[key]})`;
            } else {
                //caso haja mais de 1 pa�s com o n�mero de fronteiras = keyset[key]
                output += `${countries[country]}, `;
            }
            countries_number--;
        }
        //item da lista
        var item = document.createElement("p");
        item.innerText = `${output}`;

        if (position == 1) { //o primeiro colocado tem um CSS diferente
            item.className = "first";
        }
        div_to_append.append(item);
        position++;
    }
}