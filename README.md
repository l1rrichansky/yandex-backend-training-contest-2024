# yandex-backend-training-contest-2024
Тренировочный контекст - Бэкэнд. Яндекс.
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

