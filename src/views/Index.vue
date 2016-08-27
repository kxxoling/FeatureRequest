<template lang="jade">
.index
  h2 Feature Request
  d-panel(title="Validation Example")
    d-form(:model="user", :schema="userSchema", label-width="140", :cols="1")
      d-text-field(property="title")
      d-text-field(property="description", type="textarea", :editor-height="100")
      d-select-field(property="client")
      d-text-field(property="priority")
      d-text-field(property="date")
      d-text-field(property="url")
      d-select-field(property="area")
      d-field
        d-button(@click="submit()") Submit
</template>

<script>
import { Schema } from 'vue-desktop';

const userSchema = new Schema({
  title: {
    label: 'Title',
    required: true,
  },
  description: {
    label: 'Description',
    required: true,
  },
  client: {
    label: 'Client',
    required: true,
    mapping: {
      'Client A': 'a',
      'Client B': 'b',
      'Client C': 'c',
    },
  },
  priority: {
    label: 'Client priority',
    required: true,
  },
  date: {
    label: 'Target date',
    required: true,
    type: 'date',
    default() {
      return new Date();
    },
  },
  url: {
    label: 'Ticket URL',
    required: false,
  },
  area: {
    label: 'Product area',
    required: false,
    mapping: {
      Policies: 'policies',
      Billing: 'billing',
      Claims: 'claims',
      Reports: 'reports',
    },
  },
});

export default {
  methods: {
    validate() {
      userSchema.validate(this.user);
    },

    submit() {
      this.validate();
      const feature = this.user.toObject();
      console.log(feature);

      this.$http.post('/api/features', feature)
        .then((data) => {
          console.log(data);
        });
    },
  },

  data() {
    return {
      userSchema,
      user: userSchema.newModel(),
    };
  },
};
</script>

<style lang="stylus">

</style>
