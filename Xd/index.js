const fs = require('fs');
const possible_actions = [1, 5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125, -1, -5, -25, -125, -625, -3125, -15625, -78125, -390625, -1953125];
// const possible_actions = [1, 31, -1, -31];
const starting_nodes = [1, 2, 3 , 1953128, 3906253];
// const starting_nodes = [1];
let data = "";
let read_array = [];
let excel_array = [];

try {
    data = fs.readFileSync('./README2.txt', 'utf8').replaceAll("\n", "").split(" ");
    // data = fs.readFileSync('./README1.txt', 'utf8').replaceAll("\n", "").split(" ");
    console.log("Successfully read file README2.txt");
    read_array = data.map(Number)
} catch (err) {
    console.error(err);
}
try {
    data = fs.readFileSync('./xdpuzzle1.csv', 'utf8').replaceAll("\n", "").split(",");
    console.log("Successfully read file xdpuzzle1.csv");
    excel_array = data.map(Number)
} catch (err) {
    console.error(err);
}
// console.log(data);
console.log(read_array);
console.log(excel_array);

let possible_directories = [[9765625]];
// let possible_directories = [[961]];
// let index = 0;
console.log(checkPossibilitiesV2(possible_directories));
function checkPossibilitiesV2(input_array) {
    if (input_array.length <= 0) {
        throw new Error(`There are no possible paths ):`);
    }
    let current_number = input_array[0][input_array[0].length - 1];
    console.log(current_number);
    if (starting_nodes.includes(current_number)) {
        throw new Error(`Done! Found beginning node! ${input_array[0]}`);
    }
    // if (excel_array.includes(current_number)) {
    //     throw new Error("Found in Excel sheet!");
    // }
    for (let i in possible_actions) {
        let num_1 = current_number + possible_actions[i];
        let num_2 = num_1 + possible_actions[i];
        if (read_array.includes(num_1) && read_array.includes(num_2) && !input_array[0].includes(num_1) && !input_array[0].includes(num_2)) {
            console.log(`${num_1} (${possible_actions[i]})`);
            console.log(`${num_2} (${possible_actions[i]})`);
            let new_array = input_array[0].slice();
            new_array.push(num_1, num_2);
            input_array.splice(1, 0, new_array);
        }
    }
    input_array.shift();
    console.log(input_array);
    checkPossibilitiesV2(input_array);
}