# yandex-backend-training-contest-2024
Тренировочный контекст - Бэкэнд. Яндекс. Что смог...
<div class="header">
      <h1 class="title">A. Хитрый шифр</h1>
      <table>
         <tbody><tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>2&nbsp;секунды</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>512Mb</td>
         </tr>
         <tr class="input-file">
            <td class="property-title">Ввод</td>
            <td colspan="1">стандартный ввод или input.txt</td>
         </tr>
         <tr class="output-file">
            <td class="property-title">Вывод</td>
            <td colspan="1">стандартный вывод или output.txt</td>
         </tr>
      </tbody></table>
   </div>

   <div class="legend"> Известная компания Тындекс в очередной раз проводит набор стажёров.
      <p style="text-indent: 0em;">Заботясь о персональных данных соискателей, компания придумала хитрый алгоритм шифрования: </p><ul>
        <li>Подсчитывается количество различных символов в ФИО (регистр важен, А и а — разные символы).</li>
      <li>Берётся сумма цифр в дне и месяце рождения, умноженная на 64.</li>
      <li>Для первой (по позиции в слове) буквы фамилии определяется её номер в алфавите (в 1-индексации), умноженный на 256 (регистр буквы не важен).</li>
      <li>Полученные числа суммируются.</li>
      <li>Результат переводится в 16-чную систему счисления (в верхнем регистре).</li>
      <li>У результата сохраняются только 3 младших разряда (если значимых разрядов меньше, то шифр дополняется до 3-х разрядов ведущими нулями).</li>
      </ul>
      <p style="text-indent: 0em;">Ваша задача — помочь вычислить для каждого кандидата его шифр. </p>
      <p></p>
      
   </div>
   <h2>Формат ввода</h2>
   В первой строке вводится число N(1≤N≤10000) — количество кандидатов и шифров.
Далее следует N строк в формате CSV (fj,ij,oj,dj,mj,yj) — информация о кандидатах:
<p></p>
<ul><li>Фамилия fj, имя ij и отчество oj(1≤∣∣fj∣∣,∣∣ij∣∣,∣∣oj∣∣≤15) — строки, состоящие из латинских букв верхнего и нижнего регистра;</li>
  <li>день рождения dj, месяц рождения mj и год рождения yj — целые числа, задающие корректную дату в промежутке от 1 января 1950 года до 31 декабря 2021 года.</li>
</ul>
   <h2>Формат вывода</h2>
   
   В единственной строке выведите N строк k1, k2, …, kN, где kj — шифр j-го кандидата <b>(в верхнем регистре)</b>. Кандидаты нумеруются с 1 до N в порядке ввода.

   <h2>Пример</h2>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод<div class="problem__copy-sample"><button class="button button_theme_pseudo button_size_s button_only-icon_yes problem__copy-button problem__copy-button_type_input i-bem button_js_inited" data-bem="{&quot;button&quot;:{}}" role="button" type="button" title="Скопировать ввод"><span class="button__text">&nbsp;<img class="image button__icon button__icon_role_copy" src="//yastatic.net/lego/_/La6qi18Z8LwgnZdsAr1qy1GwCwo.gif" alt="Скопировать ввод"></span></button></div></th>
            <th>Вывод<div class="problem__copy-sample"><button class="button button_theme_pseudo button_size_s button_only-icon_yes problem__copy-button problem__copy-button_type_output i-bem" data-bem="{&quot;button&quot;:{}}" role="button" type="button" title="Скопировать вывод"><span class="button__text">&nbsp;<img class="image button__icon button__icon_role_copy" src="//yastatic.net/lego/_/La6qi18Z8LwgnZdsAr1qy1GwCwo.gif" alt="Скопировать вывод"></span></button></div></th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>2
Volozh,Arcady,Yurievich,11,2,1964
Segalovich,Ilya,Valentinovich,13,9,1964
</pre></td>
            <td><pre>710 64F 
</pre></td>
         </tr>
      </tbody>
   </table>
   <h2>Примечания</h2>
   Рассмотрим тестовый пример.
<p>Первый кандидат — Volozh,Arcady,Yurievich,11,2,1964:</p>
   <ul>
     <li> 	Различные символы в ФИО: V, o, l, z, h, A, r, c, a, d, y, Y, u, i, e, v - всего их 16.</li>
   <li> 	Сумма цифр в дне и месяце рождения равна 1+1+2= 4.</li>
   <li> 	Номер в алфавите первой буквы фамилии V равен 22.</li>
   <li> 	Итоговое значение шифра равно 16+4⋅64+22⋅256= 5904.</li>
   <li> 	В 16-ричной системе счисления это число представимо как 1710.</li>
   <li> 	Нас интересуют только 3 последние разряда, поэтому остаётся 710.</li>
   </ul><p>Второй кандидат — Segalovich,Ilya,Valentinovich,13,9,1964:</p><ul>
   <li> 	Различные символы в ФИО: S, e, g, a, l, o, v, i, c, h, I, y, V, n, t - всего их 15.</li>
   <li> 	Сумма цифр в дне и месяце рождения равна 1+3+9= 13.</li>
   <li> 	Номер в алфавите первой буквы фамилии S равен 19.</li>
   <li> 	Итоговое значение шифра равно 15+13⋅64+19⋅256= 5711.</li>
   <li> 	В 16-ричной системе счисления это число представимо как 164F.</li>
   <li> Нас интересуют только 3 последние разряда, поэтому остаётся 64F.</li>
    </ul>
<h2></h2>
<div class="header">
      <h1 class="title">B. Через тернии к клиенту</h1>
      <table>
         <thead>
            <tr><th></th>
            <th>Все языки</th>
            <th>Clang 16.0.0 C++20</th>
            <th>GNU GCC 12.2 C++20</th>
         </tr></thead>
         <tbody><tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>5&nbsp;секунд</td>
            <td>1&nbsp;секунда</td>
            <td>1&nbsp;секунда</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>512Mb</td>
            <td>512Mb</td>
            <td>512Mb</td>
         </tr>
         <tr class="input-file">
            <td class="property-title">Ввод</td>
            <td colspan="3">стандартный ввод или input.txt</td>
         </tr>
         <tr class="output-file">
            <td class="property-title">Вывод</td>
            <td colspan="3">стандартный вывод или output.txt</td>
         </tr>
      </tbody></table>
   </div>
   <h2></h2>
   <div class="legend"> Известная компания Тындекс идёт в ногу со временем — с началом активных космических перелётов в компании открылся сервис
      Тындекс.Ракетакси: пользователю необходимо лишь указать координаты начала и конца перелёта, после чего за ним вылетит персональная
      ракета. <!--l. 49-->
      <p style="text-indent: 0em;">По сути любой заказ можно описать в виде событий четырёх типов: </p><ol style="list-style-type:
      decimal;">
      <li><span style="font-weight: bold;">A </span>(accepted) - заказ принят в работу (ракета вылетела за клиентом); </li>
      <li><span style="font-weight: bold;">B </span>(boarding) - клиент сел в ракету; </li>
      <li><span style="font-weight: bold;">S </span>(success) - заказ успешно завершён (клиент вышел на планете назначения); </li>
      <li><span style="font-weight: bold;">C </span>(cancelled) - заказ отменён. </li>
      </ol>
      <!--l. 63-->
      <p style="text-indent: 0em;">Все происходящие с ракетами события отправляются на сервера, где сразу логируются. Вот только
      из-за проблем со связью (метеоритные потоки, вспышки на звездах и т.д.) отправка событий иногда затягивается, из-за чего записи
      в получившемся логе могут идти не по порядку. <!--l. 65-->
      </p><p style="text-indent: 0em;">Гарантируется, что все описанные в логе события задают один из следующих сценариев: </p><ol style="list-style-type: decimal;">
      <li><span style="font-weight: bold;">A </span>- <span style="font-weight: bold;">B </span>- <span style="font-weight: bold;">S</span></li>
      <li><span style="font-weight: bold;">A </span>- <span style="font-weight: bold;">B </span>- <span style="font-weight: bold;">C</span></li>
      <li><span style="font-weight: bold;">A </span>- <span style="font-weight: bold;">C</span></li>
      </ol>
      <!--l. 77-->
      <p style="text-indent: 0em;">Вам, как главному аналитику (и по совместительству главному программисту) ракетопарка, необходимо
      исследовать лог за прошедший год и определить для каждой ракеты суммарное время движения (в минутах) в течение заказов. <!--l.
      79-->
      </p><p style="text-indent: 0em;">В каждый момент времени ракета выполняет только один заказ. Будем считать, что каждая ракета
      в каждый момент времени: </p><ul>
      <li>или стоит на месте в ожидании заказа, </li>
      <li>или перемещается по космосу, выполняя заказ. </li>
      </ul>
      <!--l. 89-->
      <p style="text-indent: 0em;">Движение начинается после принятия заказа и завершается после отмены или завершения заказа. За
      одну минуту не может произойти несколько событий, связанных с одной и той же ракетой. </p>
      <p></p>
      <p></p>
      <p></p>
      <p></p>
      <p></p>
      
   </div>
<h2>Формат ввода</h2>
В первой строке дано целое число N(2≤N≤200000)  — количество записей в логе.
Следующие N строк содержат записи в логе в формате day hour minute id status:<p></p>
<ul>
<li>day(1≤d≤365)  — номер дня (сквозная нумерация с начала календарного года);</li>
<li>hour(0≤h<24)  — часы;</li>
<li>minute(0≤m<60)  — минуты;</li>
<li>id(0≤id≤109)  — уникальный идентификатор ракеты;</li>
<li>status∈{A,B,S,C}  — буква, обозначающая тип события.</li>
</ul>
<h2>Формат вывода</h2>
<div class="output-specification"> В единственной строке выведите через пробел суммарное время движения на заказах для каждой упомянутой в логе ракеты. Данные
      необходимо выводить в порядке возрастания идентификаторов ракет. 
   </div>
   <h2>Пример</h2>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод<div class="problem__copy-sample"><button class="button button_theme_pseudo button_size_s button_only-icon_yes problem__copy-button problem__copy-button_type_input i-bem" data-bem="{&quot;button&quot;:{}}" role="button" type="button" title="Скопировать ввод"><span class="button__text">&nbsp;<img class="image button__icon button__icon_role_copy" src="//yastatic.net/lego/_/La6qi18Z8LwgnZdsAr1qy1GwCwo.gif" alt="Скопировать ввод"></span></button></div></th>
            <th>Вывод<div class="problem__copy-sample"><button class="button button_theme_pseudo button_size_s button_only-icon_yes problem__copy-button problem__copy-button_type_output i-bem" data-bem="{&quot;button&quot;:{}}" role="button" type="button" title="Скопировать вывод"><span class="button__text">&nbsp;<img class="image button__icon button__icon_role_copy" src="//yastatic.net/lego/_/La6qi18Z8LwgnZdsAr1qy1GwCwo.gif" alt="Скопировать вывод"></span></button></div></th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>8
50 7 25 3632 A
14 23 52 212372 S
15 0 5 3632 C
14 21 30 212372 A
50 7 26 3632 C
14 21 30 3632 A
14 21 40 212372 B
14 23 52 3632 B
</pre></td>
            <td><pre>156 142
</pre></td>
         </tr>
      </tbody>
   </table>
   <h2>Примечания</h2>
   <div class="notes"><span style="font-weight: bold;">Ракета №3632</span><p></p><ol style="list-style-type: decimal;">
      <li>в 14-й день года в 21:30 получила заказ (шестая запись в логе); </li>
      <li>забрала пассажира в 23:52 того же дня (восьмая запись в логе); </li>
      <li>после чего заказ был отменён в 15-й день года в 00:05 (третья запись в логе); </li>
      <li>в 50-й день года в 7:25 получила заказ (первая запись в логе); </li>
      <li>заказ был отменён уже через минуту (четвёртая запись в логе).</li>
      </ol>
      <!--l. 124-->
      <p style="text-indent: 0em;">Таким образом ракета №3632 провела в движении с 14-го дня 21:30 до 15-го дня 00:05 и с 50-го
      дня 7:25 до 50-го дня 7:26 — всего 156 минут. <!--l. 126-->
      </p><p style="text-indent: 0em;"><span style="font-weight: bold;">Ракета №212372</span></p><ol style="list-style-type: decimal;">
      <li>в 14-й день года в 21:30 получила заказ (третья запись в логе); </li>
      <li>через 10 минут забрала пассажира (седьмая запись в логе); </li>
      <li>в 23:52 прибыла на место назначения (вторая запись в логе).</li>
      </ol>
      <!--l. 134-->
      <p style="text-indent: 0em;">Всего ракета №212372 провела в движении с 14-го дня 21:30 до 14-го дня 23:52 142 минуты. </p>
      <p></p>
      <p></p>
      
   </div>
<div class="header">
      <h1 class="title">C. Приснится же такое...</h1>
      <table>
         <thead>
            <tr><th></th>
            <th>Все языки</th>
            <th>Clang 16.0.0 C++20</th>
            <th>GNU GCC 12.2 C++20</th>
         </tr></thead>
         <tbody><tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>3&nbsp;секунды</td>
            <td>2&nbsp;секунды</td>
            <td>2&nbsp;секунды</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>512Mb</td>
            <td>512Mb</td>
            <td>512Mb</td>
         </tr>
         <tr class="input-file">
            <td class="property-title">Ввод</td>
            <td colspan="3">стандартный ввод или input.txt</td>
         </tr>
         <tr class="output-file">
            <td class="property-title">Вывод</td>
            <td colspan="3">стандартный вывод или output.txt</td>
         </tr>
      </tbody></table>
   </div>
   <h2></h2>
   <div class="WordSection1">

<p class="MsoNormal"><span style="mso-ansi-language:#2000;mso-fareast-language:
#2000">Наконец-то с царством Морфея удалось наладить дипломатические отношения!
Первым делом в магазины поступили самые корректные и полные сонники,
составленные в сотрудничестве с главными <span class="SpellE">сномагами</span>
царства.<o:p></o:p></span></p>

<p class="MsoNormal"><span style="mso-ansi-language:#2000;mso-fareast-language:
#2000">Ваш близкий друг Тирания <span class="SpellE">Вампадур</span> купила такой
сонник одной из первых. Но тут же её ждало разочарование. Оказалось, что
некоторые сны образуют целую последовательность сюжетов, которую надо
интерпретировать только целиком.<o:p></o:p></span></p>

<p class="MsoNormal"><span style="mso-ansi-language:#2000;mso-fareast-language:
#2000">И у Тирании оказалась именно такая ситуация. Когда-то давно ей
приснилось двоичное дерево из&nbsp;N&nbsp;вершин, занумерованных целыми числами
от&nbsp;1&nbsp;до&nbsp;N.<o:p></o:p></span></p>

<p class="MsoNormal"><span style="mso-ansi-language:#2000;mso-fareast-language:
#2000">Вершина&nbsp;1&nbsp;являлась корнем. У каждой вершины&nbsp;v&nbsp;было
до двух сыновей: левый имел номер&nbsp;2</span><span style="font-family:&quot;Cambria Math&quot;,serif;
mso-bidi-font-family:&quot;Cambria Math&quot;;mso-ansi-language:#2000;mso-fareast-language:
#2000">⋅</span><span style="mso-ansi-language:#2000;mso-fareast-language:
#2000">v, правый —&nbsp;2</span><span style="font-family:&quot;Cambria Math&quot;,serif;
mso-bidi-font-family:&quot;Cambria Math&quot;;mso-ansi-language:#2000;mso-fareast-language:
#2000">⋅</span><span style="mso-ansi-language:#2000;mso-fareast-language:
#2000">v+1&nbsp;(при условии, что их номера не превосходили&nbsp;N). Таким
образом, зная число&nbsp;N, дерево можно было однозначно восстановить.<o:p></o:p></span></p>

<p class="MsoNormal"><span style="mso-ansi-language:#2000;mso-fareast-language:
#2000">Но, к сожалению, следующие&nbsp;Q&nbsp;ночей Тирании снились похожие
сны: одна из вершин дерева&nbsp;v&nbsp;менялась местами с её предком
(если&nbsp;v&nbsp;была корнем дерева, то ничего не происходило). Причем эти
изменения переносились между снами, всё больше и больше изменяя оригинальное
дерево.<o:p></o:p></span></p>

<p class="MsoNormal"><span style="mso-ansi-language:#2000;mso-fareast-language:
#2000">Чтобы верно интерпретировать значение снов, Тирании нужно узнать
итоговую структуру дерева после всех произошедших с ним изменений. Она просит
вас помочь ей и по последовательности менявшихся вершин найти итоговую
структуру дерева из её снов.<o:p></o:p></span></p>

<p class="MsoNormal"><span style="mso-ansi-language:#2000;mso-fareast-language:
#2000">Понимая, что в этом деле важна точность, вы расспросили Тиранию насчет
процесса обмена местами вершины&nbsp;v&nbsp;с её предком.<o:p></o:p></span></p>

<p class="MsoNormal"><span style="mso-ansi-language:#2000"><o:p>&nbsp;</o:p></span></p>

</div>

![image](https://github.com/l1rrichansky/yandex-backend-training-contest-2024/assets/85824228/c8f6bcda-8c9f-471d-8548-58c8d1f8f5ff)
![image](https://github.com/l1rrichansky/yandex-backend-training-contest-2024/assets/85824228/bbced84d-c630-4925-bbad-cf7a39647254)
![image](https://github.com/l1rrichansky/yandex-backend-training-contest-2024/assets/85824228/b8433e2b-7057-498c-83a4-caac1c37fb91)
![image](https://github.com/l1rrichansky/yandex-backend-training-contest-2024/assets/85824228/6d05387d-3100-4cd1-bffc-9f236ce8d288)
![image](https://github.com/l1rrichansky/yandex-backend-training-contest-2024/assets/85824228/5c261a55-73c4-439f-ab82-bcf700101dd4)
![image](https://github.com/l1rrichansky/yandex-backend-training-contest-2024/assets/85824228/e12c9c14-f173-44af-92b8-8553a37b3e0b)
![image](https://github.com/l1rrichansky/yandex-backend-training-contest-2024/assets/85824228/1c296d1c-afc5-4d66-8db0-02e93762a831)
![image](https://github.com/l1rrichansky/yandex-backend-training-contest-2024/assets/85824228/8fa161be-2b28-4e55-95e3-157861fe4293)
![image](https://github.com/l1rrichansky/yandex-backend-training-contest-2024/assets/85824228/6a13aa99-ec34-4147-a584-8b808f8fe4e6)
![image](https://github.com/l1rrichansky/yandex-backend-training-contest-2024/assets/85824228/7e644333-3248-4870-a2ec-6f0de8c97807)
![image](https://github.com/l1rrichansky/yandex-backend-training-contest-2024/assets/85824228/a0e30da0-02e9-4fdd-a78e-13c70078204f)


