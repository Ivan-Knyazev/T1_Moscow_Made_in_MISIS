import React from "react";
import "./styles.css";

const DigitalAssistant = () => {
  return (
    <div className="container">
      {/* Общие фразы */}
      <section>
        <h2>Общие фразы</h2>
        <div style={{ display: "flex", gap: "20px", flexWrap: "wrap" }}>
          <label style={{ flex: "1" }}>
            Приветствие
            <input type="text" placeholder="Добрый день!" />
          </label>
          <label style={{ flex: "1" }}>
            Завершение диалога
            <input type="text" placeholder="Рад был помочь!" />
          </label>
          <label style={{ flex: "1" }}>
            Описание ассистента
            <textarea placeholder="Я отвечу на ваши вопросы и помогу разобраться в нашем продукте." />
          </label>
        </div>
      </section>

      {/* База знаний */}
      <section>
        <h2>База знаний</h2>
        <div style={{ display: "flex", gap: "20px", flexWrap: "wrap" }}>
          <label style={{ flex: "1" }}>
            Тип базы знаний
            <select>
              <option value="file">Файл</option>
              <option value="url">URL</option>
            </select>
          </label>
          <label style={{ flex: "1" }}>
            Промпт для ассистента
            <input type="text" placeholder="Дружелюбный стиль общения" />
          </label>
          <label style={{ flex: "1" }}>
            Модель нейронной сети
            <select>
              <option value="GPT">GPT</option>
              <option value="BERT">BERT</option>
              <option value="Custom">Custom</option>
            </select>
          </label>
          <label style={{ flex: "1" }}>
            Загрузить файл базы знаний
            <input type="file" />
          </label>
        </div>
      </section>

      {/* Внешний вид */}
      <section>
        <h2>Внешний вид</h2>
        <div style={{ display: "flex", gap: "20px", flexWrap: "wrap" }}>
          <label style={{ flex: "1" }}>
            Цвета
            <div style={{ display: "flex", gap: "10px", marginTop: "5px" }}>
              <input type="color" value="#4EA3B2" />
              <input type="color" value="#D8E6E8" />
              <input type="color" value="#000000" />
            </div>
          </label>
          <label style={{ flex: "1" }}>
            Шрифт
            <select>
              <option value="Rubik">Rubik</option>
              <option value="Montserrat">Montserrat</option>
              <option value="Inter">Inter</option>
            </select>
          </label>
          <label style={{ flex: "1" }}>
            Имя ассистента
            <input type="text" placeholder="Цифровой ассистент" />
          </label>
          <label style={{ flex: "1" }}>
            Загрузить аватар ассистента
            <input type="file" />
          </label>
        </div>
      </section>

      {/* Цифровой ассистент */}
      <section>
        <h2>Цифровой ассистент</h2>
        <div className="assistant-box">
          <p>Добрый день!</p>
          <p>Я отвечу на ваши вопросы и помогу разобраться в нашем продукте.</p>
          <p>Как собрать домик для кошки?</p>
        </div>
        <input
          type="text"
          placeholder="Введите сообщение"
          className="chat-input"
        />
      </section>
    </div>
  );
};

export default DigitalAssistant;
