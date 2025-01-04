document.addEventListener("DOMContentLoaded", () => {
    const velikost_mrizky = 15;
    let hrac = 'X'; //zacainaj krizky
    let stav = Array(velikost_mrizky).fill(null).map(() => Array(velikost_mrizky).fill(null));
    
    const mrizka_js = document.getElementById("mrizka");

    // mtizka
    function vytvoreni_mrizky() {
        for (let i = 0; i < velikost_mrizky; i++) {
            let row = mrizka_js.insertRow();
            for (let j = 0; j < velikost_mrizky; j++) {
                let bunka = row.insertCell();
                bunka.classList.add('empty');
                bunka.addEventListener('click', () => kliknuti(i, j, bunka));
            }
        }
    }

    // kliknuti na bunku
    function kliknuti(i, j, bunka) {
        if (stav[i][j] !== null) return; // plno -> nic se nestane

        stav[i][j] = hrac;
        bunka.classList.remove('empty');
        bunka.classList.add(hrac.toLowerCase());
        bunka.textContent = hrac === 'X' ? 'X' : 'O'; // vlozeni krizku nebo kolecka

        if (kontrola_vyhry(i, j)) {
            alert(`${hrac} je vítěz!!!`);
            resetovani();
        } else {
            hrac = hrac === 'X' ? 'O' : 'X';
        }
    }

    // kotrola viteze
    function kontrola_vyhry(i, j) {
        return kontrola_smeru(i, j, 1, 0) || // hor
               kontrola_smeru(i, j, 0, 1) || // ver
               kontrola_smeru(i, j, 1, 1) || // smer /
               kontrola_smeru(i, j, 1, -1);  // smer \
    }

    function kontrola_smeru(i, j, di, dj) {
        let count = 1;

        // kontrola v jednom smeru
        for (let step = 1; step < 5; step++) {
            const ni = i + step * di;
            const nj = j + step * dj;
            if (ni < 0 || ni >= velikost_mrizky || nj < 0 || nj >= velikost_mrizky || stav[ni][nj] !== hrac) break;
            count++;
        }

        // v opacnym
        for (let step = 1; step < 5; step++) {
            const ni = i - step * di;
            const nj = j - step * dj;
            if (ni < 0 || ni >= velikost_mrizky || nj < 0 || nj >= velikost_mrizky || stav[ni][nj] !== hrac) break;
            count++;
        }

        return count >= 5;
    }

    function resetovani() {
        stav = Array(velikost_mrizky).fill(null).map(() => Array(velikost_mrizky).fill(null));
        hrac = '✖️';
        mrizka_js.innerHTML = '';
        vytvoreni_mrizky();
    }

    vytvoreni_mrizky();
});
