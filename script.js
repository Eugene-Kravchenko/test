 'use strict' //говорит о том что мы работаем по сандартам ES 6
 console.log(leftBorferWidt); 
var leftBorferWidt = 1;     //эта переменная объявлена во всем коде и даже если ее выводить до самого объявления 
//комп будет видеть переменную, просто пустую
//var - переменная
let second = 2; //let создается только тогда когда код до нее доходит
// еще console.log не сможет её найти если ее засунуть в фигурные скобки и также она экономичней в плане сохранения памяти
const pi = 3.14;

var number = 5; //номер
var string = "Hello"; //строка
var sym = Symbol() //символ -_ -
var boolean = true; //логический true и false
null; //то чего не существует в коде.
undefined; //существует, но эта переменная или
// чтобы там ни было не имеет никакого значения

var obj = {}; //объект. Коллекция данных. Типа контейнера в питоне

//ОБЪЕКТ - - - - - - - -- -  - - - - - - - -
let persone = {
    name: "John",
    age: 25,
    isMarried: false
};
// обратиться к элементам объекта можно с помощью точки или кв скобок
//достаем из объекта:

console.log(persone.name);
console.log(persone["name"]); // исп для больших названий и хз почему точка так не может

// Массивы. Используются для хранения данных которпые идут по порядку
// заключается в кв скобки и построен так, что каждому значению в нем
// автоматически присваивается порядковый номер

//МАССИВ - - - - - -- - - -  - - - - - - - - - - - - - - - 
let arr = ['plum.png', 'orange.jpg', 'apple.bmp'];

// Обращаемся к массиву:
console.log(arr[2]);

// alert("hello mir"); //выводит в браузере. Простейшее модальное окно. После подтверждения (ок) остальные скрипты срабатывают только после этого

// let answer = confirm('are u human??'); //ПОДТВЕРЖДЕНИЕ. ОН СПРАШИВАЕТ И У ПОЛЬЗОВАТЕЛЯ ЕСТЬ 2 КНОПКИ ВЫБОРА
// console.log (answer); //если ответишь да то true получишь в консоль, если же нет то false

// let answer = prompt ('вам уже есть 124?', 'ну да.'); //prompt позволяет вводить текст в всплывающее окно и показывать текст который может там находиться по дефолту
// console.log (answer); //это запишет инФормациютого, что ответил пользователь 

//console.log(typeof(answer));//это позволяет узнать тип текста, строка или номер и тп..


            //ОПЕРАТОРЫ

// console.log("hey"+" gay"); //строка + строка = строка
// console.log(5 +" gay"); //число + строка = строка

    //>Если перед prompt поставить "+", то априоре текстовое значение превратится в числовое
    //Даже если там будут буквы<

    // let answer = prompt ('вам уже есть 124?', 'ну да.');
    // console.log (typeof(answer));
//---------------------------------------------------------------------------------------------------------------
// let incr = 10,
//     decr = 10;

// incr++; //инкремент увеличил число на 2 
// decr--; //декримент уменьшил число на 2 

// console.log(incr);
// console.log(decr);
//---------------------------------------------------------------------------------------------------------------
// console.log(5%2); //остаток деления 5 на 2
console.log("1" == 1);//TRUE потому что двойное равенство сравнивает по значениям 
console.log("1" === 1);// FALSE потому что  в тройном равенстве идет сравнение по типам данных

//------------------------------------------------------------------------------------------------------
//Для операций над логическими значениями в JavaScript есть || (ИЛИ), && (И) и ! (НЕ).

let a = true;
    b = true;
console.log(a && b);  // (&& - и) если и там и там true -> true
console.log(a || b);  // (|| - или) если хотя бы 1 из элементов явлется true то -> true
console.log(a && !b);  // (! - отрицание) реверсит значение если было true то станет false