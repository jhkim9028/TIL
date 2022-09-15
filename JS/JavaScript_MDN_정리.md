# JavaScript

웹 페이지를 위한 스크립트 언어로 잘 알려져있지만, Node.js, Apache CouchDB, Adobe Acrobat처럼 많은 비 브라우저환경에서도 사용하고 있습니다.

## 변수

변수란,숫자 또는 문자열 과 같은 값의 컨테이너.

변수에 포함된 값이 변경될 수 있다는 특징이 있다.

```html
<button>Press me</button>
```

```js
const button = document.querySelector('button');

button.onclick = function() {
    let name = propt('What is your name?');
    alert('Hello' + name + ', nice to see you!');
}
```

독자가 이름을 입력하도록 요청한 화면에 상자를 띄운 다음, 변수에 값을 저장합니다.

변수 값에서 가져온, 이름이 포함된 환영 메시지가 표시됩니다.

변수는 값을 포함하고 있습니다. 변수는 값 자체가 아닙니다. 이것은 중요한 차이점입니다.

변수는 값을 위한 컨테이너입니다. 물건들을 저장할 수 있는 작은 상자와 같다고 생각할 수 있습니다.

```js
var myName;
var myAge;
```

두 변수는 값을 포함하지 않는 빈 컨테이너입니다. 변수 이름만 입력할 경우 undefined 값을 반환하며 변수는 이 값을 포함하게 됩니다.

```js
var myName = 'Chris';
```

## 변수 이름

바람직한 변수 이름의 예:

- age

- myAge

- init

- initialColor

- finalOutputValue

- audio1

- audio2

바람직하지 않은 변수 이름의 예:

- 1

- a

- _12

- myage

- MYAGE

- var

- Document

- skjfndskjfnbdskjfb

- thisisareallylongstupidvariablenameman

### 변수의 종류

- 숫자

- 문자열

- 불리언
  
  - ```js
    var test = 6 > 3;
    
    // "<"연산자를 사용해서 6이 3보다 작은지를 확인합니다.
    // 예상한대로 6이 3보다 작지 않으므로 false를 반환합니다.
    ```

- 배열
  
  - ```js
    var myNameArray = ['Chris', 'Bob', 'Jim'];
    var myNumberArray = [10,15,40];
    
    myNameArray[0]; // should return 'Chris'
    myNumberArray[2]; // should return 40
    ```

- 객체
  
  - ```js
    var dog = { name : 'Spot', breed : 'Dalmatian' };
    
    // 객체에 저장된 정보를 검색하기 위해서는 아래 구문을 사용합니다.
    dog.name
    ```

## 숫자와 연산자

정수는 10,100, -5같은 모든 숫자입니다.

부동소수점 실수(floor)는 12.5, 4.67734과 같은 소수점과 소수 자릿수가 있습니다.

배정밀도 부동소수점 실수(double) 부동 소수점보다 더 정확한 정밀도를 가지고 있는 특별한 데이터 타입입니다.

#### == vs ===

Equality

== 와 != 는 Rquality 연산자이다. JS에서 ==를 사용하면 연산이 되기 전에 피연산자들을 먼저 비교할 수 있는 형태로 변환시킨다.

따라서 == 를 사용하면 다음과 같은 사실이 성립한다.

```js
254 == '254'                // return true
true == 1                   // return true
undefined == null           // return true
'abc' == new String('abc')  // return true
null == false               // return false
'true' == true              // return false
true == 2                   // return false
```

Identity

=== 와 !==는 Identity 연산자이다. 이 녀석은 ==와는 반대로 형변환을 하지 않고 연산한다.

```js
254 === '254'               // return false
true === 1                  // return false
undefined === null          // return false
'abc' === new String('abc') // return false
```

## JS 구성요소

- [조건문](./조건문.md)

- [반복문](./반복문.md)


