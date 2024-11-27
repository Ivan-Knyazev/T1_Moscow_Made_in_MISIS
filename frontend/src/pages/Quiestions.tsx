import React from "react";

const Questions = ({ state, setState }) => {
  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    console.log("Отправка данных формы:", state);

    fetch("https://example.com", {
      method: "POST", // Изменено на POST
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(state),
    })
      .then((res) => res.json())
      .then((data) =>
        setState((prev) => ({
          ...prev,
          pos: 3,
          greeting: "",
          farevell: "",
          disc: "",
          link_bd: "",
          promt: "",
          model_ai: "",
          file_bd: null,
          color: "rgba(78, 163, 178, 1)",
          font: "Rubik",
          name: "",
          avatar: null,
          res: data,
        }))
      )
      .catch((error) => console.error("Ошибка:", error));
  };

  const handleInputChange =
    (key: string) =>
    (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
      setState((prev) => ({
        ...prev,
        [key]: e.target.value,
      }));
    };

  const handleFileChange =
    (key: string) => (e: React.ChangeEvent<HTMLInputElement>) => {
      const file = e.target.files?.[0] || null;
      setState((prev) => ({
        ...prev,
        [key]: file,
      }));
    };

  return (
    <form onSubmit={handleSubmit}>
      <div className="wrap">
        <div className="block">
          <h2>Общие фразы</h2>
          <div className="second-flex" style={{ gap: "20px" }}>
            <div className="third-flex" style={{ gap: "12px" }}>
              <label>
                Приветствие
                <input type="text" onChange={handleInputChange("greeting")} />
              </label>
              <label>
                Завершение диалога
                <input type="text" onChange={handleInputChange("farevell")} />
              </label>
            </div>
            <label>
              Описание
              <input type="text" onChange={handleInputChange("disc")} />
            </label>
          </div>
        </div>

        <div className="block">
          <h2>База знаний</h2>
          <div className="second-flex" style={{ gap: "20px" }}>
            <div className="third-flex" style={{ gap: "12px" }}>
              <label>
                URL-ссылка на базу знаний
                <input type="text" onChange={handleInputChange("link_bd")} />
              </label>
              <label>
                Промпт для ассистента
                <input type="text" onChange={handleInputChange("promt")} />
              </label>
              <label>
                Модель нейронной сети
                <select onChange={handleInputChange("model_ai")}>
                  <option value="1">Option 1</option>
                  <option value="2">Option 2</option>
                  <option value="3">Option 3</option>
                </select>
              </label>
            </div>
            <label>
              Загрузить файл базы знаний
              <input type="file" onChange={handleFileChange("file_bd")} />
            </label>
          </div>
        </div>

        <div className="block">
          <h2>Внешний вид</h2>
          <div className="second-flex" style={{ gap: "20px" }}>
            <div className="third-flex" style={{ gap: "12px" }}>
              <label>
                Цвета
                <input
                  type="color"
                  onChange={handleInputChange("color")}
                  value={state.color}
                />
              </label>
              <label>
                Шрифт
                <select onChange={handleInputChange("font")} value={state.font}>
                  <option value="Rubik">Rubik</option>
                  <option value="Montserrat">Montserrat</option>
                  <option value="Inter">Inter</option>
                </select>
              </label>
              <label>
                Имя ассистента
                <input type="text" onChange={handleInputChange("name")} />
              </label>
            </div>
            <label>
              Загрузить аватар ассистента
              <input type="file" onChange={handleFileChange("avatar")} />
            </label>
          </div>
        </div>

        <button type="submit">Готово</button>
      </div>
    </form>
  );
};

export default Questions;
