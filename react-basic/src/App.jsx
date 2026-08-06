import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'

export default function App() {
  const [form, setForm] = useState({
                            "title":"", 
                            "price":"", 
                            "isbn":"", 
                          })
  const handleFormChange = (e) => {
    const {name, value} = e.target
    console.log(name, value)
    setForm({...form, [name]:value })
  }     
  
  console.log(form)

  return (
    <>
      <h2>도서 관리 프로그램</h2>
      <form>
        <ul>
          <li>
            <label>제목</label>
            <input  type="text" 
                    name='title'
                    onChange={handleFormChange}></input>
          </li>
          <li>
            <label>가격</label>
            <input  type="text" 
                    name='price'></input>
          </li>
          <li>
            <label>ISBN</label>
            <input  type="text" 
                    name='isbn'></input>
          </li>
          <li>
            <button type="submit">등록</button>
          </li>
        </ul>
      </form>
    </>
  )
}


