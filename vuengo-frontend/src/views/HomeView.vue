<template>
  <div class="home">
    <h1 class="title is-1 is-spaced">Vuengo</h1>
    <hr />
    <div class="column is-full">
      <div class="">
        <form v-on:submit.prevent="addTask">
          <h2 class="subtitle">Add task</h2>

          <div class="field">
            <label class="label">Description</label>
            <div class="control">
              <input type="text" class="input" v-model="description" />
            </div>
          </div>

          <div class="field">
            <label for="" class="label">Status</label>
            <div class="control">
              <div class="select">
                <select v-model="status" name="" id="">
                  <option value="todo">To do</option>
                  <option value="done">Done</option>
                </select>
              </div>
            </div>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-link">Submit</button>
            </div>
          </div>
        </form>
      </div>
    </div>

    <div class="tile is-ancestor">
      <div class="tile is-parent is-6">
        <div class="todo tile is-child">
          <h2 class="subtitle is-2">To do</h2>
          <div class="card" v-for="task in tasks" v-bind:key="task.id">
            <div v-if="task.status === 'todo'">
              <div class="card-content">
                {{ task.description }}
              </div>
              <footer class="card-footer">
                <a
                  href=""
                  class="card-footer-item"
                  @click="setStatus(task.id, 'done')"
                  >Done</a
                >
              </footer>
            </div>
          </div>
        </div>
      </div>
      <div class="tile is-parent is-6">
        <div class="done tile is-child">
          <h2 class="subtitle is-2">Done</h2>

          <div class="card" v-for="task in tasks" v-bind:key="task.id">
            <div v-if="task.status === 'done'">
              <div class="card-content">
                {{ task.description }}
              </div>
              <footer class="card-footer">
                <a
                  href=""
                  class="card-footer-item"
                  @click="setStatus(task.id, 'todo')"
                  >Todo</a
                >
              </footer>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "HomeView",
  data() {
    return {
      tasks: [],
      description: "",
      status: "todo",
    };
  },
  mounted() {
    this.getTasks();
  },
  methods: {
    getTasks() {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/tasks/",
        auth: {
          username: "admin",
          password: "vuengoadmin",
        },
      }).then((response) => (this.tasks = response.data));
    },
    addTask() {
      if (this.description) {
        axios({
          method: "post",
          url: "http://127.0.0.1:8000/tasks/",
          data: {
            description: this.description,
            status: this.status,
          },
          auth: {
            username: "admin",
            password: "vuengoadmin",
          },
        })
          .then((response) => {
            let newTask = {
              id: response.data.id,
              description: this.description,
              status: this.status,
            };

            this.tasks.push(newTask);

            this.description = "";
            this.status = "todo";
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
    setStatus(task_id, status) {
      const task = this.task.filter((task) => task.id === task_id)[0];
      const description = !task.description;

      axios({
        method: "put",
        url: "http://127.0.0.1:8000/tasks/" + task_id + "/",
        headers: {
          "Content-Type": "application/json",
        },
        data: {
          status: status,
          description: description,
        },
        auth: {
          username: "admin",
          password: "vuengoadmin",
        },
      }).then(() => {
        task.status = status;
      });
    },
  },
};
</script>

<style lang="scss">
@import "/node_modules/bulma";

.select,
select {
  width: 100%;
}
.card {
  margin-bottom: 20px;
}

.done {
  opacity: 0.3;
}
.columns {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.title {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.subtitle {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
</style>
