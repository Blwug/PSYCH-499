function inflation(inflate, years) {
    let tot = (inflate / 100) * years;
    console.log("total inflation amount is", tot, "given", years, "years");
    return tot;
}

function convertedVals(orgMoney, moon, currency) {
    let newTot = orgMoney * moon;
    newTot = orgMoney + newTot;
    newTot = newTot * currency;
    console.log("We changed the original value from", orgMoney, "to", newTot);
    return newTot;
}

function staircaseA(A, mi = 0, ma = 10) {
    let c = Math.floor(Math.random() * (ma - mi + 1)) + mi;
    if (c <= 5) {
        A = A * 1.5;
        return A;
    } else {
        return A;
    }
}

function staircaseB(B) {
    B = B * 0.5;
    return B;
}

function personsChoice(initMoney, A, B, C, D, E) {
    if (A === 1) {
        A = staircaseA(initMoney);
    } else if (A === 0) {
        A = staircaseB(initMoney);
    }
    if (B === 1) {
        B = staircaseA(A);
    } else if (B === 0) {
        B = staircaseB(A);
    }
    if (C === 1) {
        C = staircaseA(B);
    } else if (C === 0) {
        C = staircaseB(B);
    }
    if (D === 1) {
        D = staircaseA(C);
    } else if (D === 0) {
        D = staircaseB(C);
    }
    if (E === 1) {
        E = staircaseA(D);
    } else if (E === 0) {
        E = staircaseB(D);
    }
    let tot = E;
    return tot;
}

let inflate = inflation(4.14, 5);
console.log(inflate);

let initial = convertedVals(160, inflate, 1.46);
console.log(initial);

let initial1 = personsChoice(initial, 1, 1, 1, 1, 1);
let initial2 = personsChoice(initial, 1, 1, 1, 0, 1);
let initial3 = personsChoice(initial, 1, 1, 0, 1, 1);
let initial4 = personsChoice(initial, 1, 1, 0, 0, 1);
let initial5 = personsChoice(initial, 1, 0, 1, 1, 1);
let initial6 = personsChoice(initial, 1, 0, 1, 0, 1);
let initial7 = personsChoice(initial, 1, 0, 0, 1, 1);
let initial8 = personsChoice(initial, 1, 0, 0, 0, 1);
let initial9 = personsChoice(initial, 0, 1, 1, 1, 1);
let initial10 = personsChoice(initial, 0, 1, 1, 0, 1);
let initial11 = personsChoice(initial, 0, 1, 0, 1, 1);
let initial12 = personsChoice(initial, 0, 1, 0, 0, 1);
let initial13 = personsChoice(initial, 0, 0, 1, 1, 1);
let initial14 = personsChoice(initial, 0, 0, 1, 0, 1);
let initial15 = personsChoice(initial, 0, 0, 0, 1, 1);
let initial16 = personsChoice(initial, 0, 0, 0, 0, 1);
let initial17 = personsChoice(initial, 0, 1, 1, 1, 1);
let initial18 = personsChoice(initial, 0, 1, 1, 0, 1);
let initial19 = personsChoice(initial, 0, 1, 0, 1, 1);
let initial20 = personsChoice(initial, 0, 1, 0, 0, 1);
let initial21 = personsChoice(initial, 0, 1, 1, 1, 1);
let initial22 = personsChoice(initial, 0, 1, 1, 0, 1);
let initial23 = personsChoice(initial, 0, 1, 0, 1, 1);
let initial24 = personsChoice(initial, 0, 1, 0, 0, 1);
let initial25 = personsChoice(initial, 0, 0, 1, 1, 1);
let initial26 = personsChoice(initial, 0, 0, 1, 0, 1);
let initial27 = personsChoice(initial, 0, 0, 0, 1, 1);
let initial28 = personsChoice(initial, 0, 0, 0, 0, 1);
let initial29 = personsChoice(initial, 0, 1, 1, 1, 1);
let initial30 = personsChoice(initial, 0, 1, 1, 0, 1);
let initial31 = personsChoice(initial, 0, 1, 0, 1, 1);
let initial32 = personsChoice(initial, 0, 1, 0, 0, 1);
console.log(initial1, initial32);
console.log("HAHAHA");


