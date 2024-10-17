import axios from "axios";

axios.defaults.baseURL = 'https://chore-planner-b346832e027b.herokuapp.com/'
axios.defaults.headers.post['Content-Type'] = 'multipart/form-data'
axios.defaults.withCredentials = true