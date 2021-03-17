import React, { Component } from "react";
// import Modal from "./components/Modal";
import axios from "axios";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      viewCompleted: false,
      todoList: [],
      modal: false,
      activeItem: {
        title: "",
        description: "",
        completed: false,
      },
      head: null,
      body:null,
      combinationList: [],
      headLink: "head.png",
      bodyLink: "body.png",
      combination:"none.png"
    };
  }

  componentDidMount() {
    this.refreshList();
  }

  refreshList = () => {
    axios
      .get("http://localhost:8000/api/posts/")
      .then((res) => this.setState({ combinationList: res.data }))
      .catch((err) => console.log(err));
  };

pickedHandler1 = (event) => {
  if (event.target.files && event.target.files.length === 1) {
      const pickedFile = event.target.files[0];
      this.setState({head:pickedFile})
      this.fileChanged1(pickedFile)
  }
};

  fileChanged1 = (file) => {
    const fileReader = new FileReader();
        fileReader.onload = () => {
            this.setState({ headLink: fileReader.result });
        };
        fileReader.readAsDataURL(file);
  }

  pickedHandler2 = (event) => {
    if (event.target.files && event.target.files.length === 1) {
        const pickedFile = event.target.files[0];
        this.setState({body:pickedFile})

        this.fileChanged2(pickedFile)
    }
  };
  
    fileChanged2 = (file) => {
      const fileReader = new FileReader();
          fileReader.onload = () => {
              this.setState({ bodyLink: fileReader.result });
          };
          fileReader.readAsDataURL(file);
    }

  upload = () => {
    const data1 = new FormData();
    data1.append("title", "head");
    data1.append("content", "head");
    data1.append("image", this.state.head);
    const data2 = new FormData();
    data2.append("title", "body");
    data2.append("content", "body");
    data2.append("image", this.state.body);
    if(!this.state.head||!this.state.body)alert('Please select files!')
    else
    axios
      .post("http://localhost:8000/api/posts/", data1, {
        // receive two parameter endpoint url ,form data
      })
      .then((res) => {
        // then print response status
        console.log(res);
      });
      axios
      .post("http://localhost:8000/api/posts/", data2, {
        // receive two parameter endpoint url ,form data
      })
      .then((res) => {
        // then print response status
        console.log(res);
        let len= "http://localhost:8000/static/human.png?"+ Math.random().toString();
        console.log(len);
        this.setState({combination: len})
      });
  };
  render() {
    return (
      <main className="container">
        <h1 className="text-white text-uppercase text-center my-4">
          Head and Body
        </h1>
        <div className="row ">
          <div className="col-md-4">
            <div className="upload-form mx-auto">
              <div className="row mb-3 ">
                <div className="col-12">
                <input type="file" onChange={this.pickedHandler1}></input>
                  <div className="row col">
                    <img
                      className="mx-auto mb-2"
                      alt="head"
                      src={this.state.headLink}
                      width="200"
                      height="200"
                    ></img>
                  </div>
                </div>
              </div>
              <div className="row ">
                <input type="file" onChange={this.pickedHandler2}></input>
                <div className="col-12">
                  <div className="row col" >
                    <img
                      className="mx-auto mb-2"
                      alt="body"
                      src={this.state.bodyLink}
                      width="200"s
                      height="200"
                    ></img>
                  </div>
                  <div className="row col">
                    <button className="btn btn-success mx-auto" onClick={this.upload}>Combine</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div className="col-md-6 upload-form">
            <div className="row w-100 he-100">
              <img className="mx-auto" alt="head" src={this.state.combination} width="200"></img>
            </div>
          </div>
        </div>
        <div className="row"></div>

        {/* <h1 className="text-white text-uppercase text-center my-4">Todo app</h1>
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <div className="mb-4">
                <button className="btn btn-primary" onClick={this.createItem}>
                  Add task
                </button>
              </div>
              {this.renderTabList()}
              <ul className="list-group list-group-flush border-top-0">
                {this.renderItems()}
              </ul>
            </div>
          </div>
        </div>
        {this.state.modal ? (
          <Modal
            activeItem={this.state.activeItem}
            toggle={this.toggle}
            onSave={this.handleSubmit}
          />
        ) : null} */}
      </main>
    );
  }
}

export default App;
