const rootElement = document.getElementById('root')

class ShoppingList extends React.Component { 
  render() { 
    return (
      <div className="shopping-list">
        Hi
      </div>
    );
  } 
}

// Create a function to wrap up your components
function App(){
  return(
  <div>
    <ShoppingList/>
  </div>
  )
}

// Use the ReactDOM.render to show your component on the browser
ReactDOM.render(
  <App/>,
  rootElement
)