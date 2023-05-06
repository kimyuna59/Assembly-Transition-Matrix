# Assembly-Transition-Matrix

## 문제 소개
분해되어있는 조각들을 하나의 완제품으로 조립하려고 한다. 조립되는 과정은 matrix로 표현된다. 이 matrix를 자동으로 생성할 수 있는 코드를 구현하시오.
- 아래의 이미지에서 A,B,C,D 네 개의 분해된 조각들을 하나로 조립하는 예시를 생각해보자.
  - 처음의 상태를 A/B/C/D 라고 하자. ('/'는 물리적으로 떨어져 있는 것을 의미함)
  - 다음 상태는 AB/C/D, AC/B/D, BC/A/D, CD/A/B 가 될 수 있다. (다음 상태로 넘어갈 때는 조각 하나씩만 붙일 수 있음)
  - AB/C/D 와 AC/B/D 와 BC/A/D 의 경우 다음 상태는 ABC/D 가 될 수 있고, AC/B/D 와 CD/A/B 의 경우 다음 상태는 ACD/B 가 될 수 있고, BC/A/D 와 CD/A/B 의 경우 다음 상태는 BCD/A 가 될 수 있다.
  - 마지막 상태는 ABCD 가 되어야 한다.

## Assembly-Transition-Matrix 예시 이미지
<p align="center">
<img src="https://user-images.githubusercontent.com/129838827/236609380-bd8b6359-6c4f-48ef-a06b-2cd2b7de6074.png">
</p>

## input 데이터의 예시 이미지
<p align="center">
<img src="https://user-images.githubusercontent.com/129838827/236611773-4aac4dcd-c3b1-4af7-b713-012e6a78b4f5.png">
</p>

## output matrix의 예시 이미지
<p align="center">
<img src="https://user-images.githubusercontent.com/129838827/236611880-22974c92-8e6c-4f39-8d90-d0b1c649be33.png">
</p>
