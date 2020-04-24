const rootElement = document.getElementById('root')

// Create a function to wrap up your components
function App() {
  return (
  <div>
    <PasteForm />
  </div>
  )
}

// Use the ReactDOM.render to show your component on the browser
ReactDOM.render(
  <App />,
  rootElement
)