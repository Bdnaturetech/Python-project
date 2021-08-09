{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "pdf_converter.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNwT3Bsk7sR6N84oUoXCNAy",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Bdnaturetech/Python-project/blob/main/pdf_converter.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GR-VRBlJUPQh",
        "outputId": "2fd8ab53-6f80-4109-df9a-1027a83c1d30"
      },
      "source": [
        "pip install tabula-py"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Requirement already satisfied: tabula-py in /usr/local/lib/python3.7/dist-packages (2.2.0)\n",
            "Requirement already satisfied: distro in /usr/local/lib/python3.7/dist-packages (from tabula-py) (1.6.0)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.7/dist-packages (from tabula-py) (1.19.5)\n",
            "Requirement already satisfied: pandas>=0.25.3 in /usr/local/lib/python3.7/dist-packages (from tabula-py) (1.1.5)\n",
            "Requirement already satisfied: python-dateutil>=2.7.3 in /usr/local/lib/python3.7/dist-packages (from pandas>=0.25.3->tabula-py) (2.8.1)\n",
            "Requirement already satisfied: pytz>=2017.2 in /usr/local/lib/python3.7/dist-packages (from pandas>=0.25.3->tabula-py) (2018.9)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.7/dist-packages (from python-dateutil>=2.7.3->pandas>=0.25.3->tabula-py) (1.15.0)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OMALzjFiNo8G",
        "outputId": "7ac36036-33a2-4a6c-b5bd-b07a73e8bdd3"
      },
      "source": [
        "!apt-get install -y xvfb # Install X Virtual Frame Buffer\n",
        "import os\n",
        "os.system('Xvfb :1 -screen 0 1600x1200x16  &')    # create virtual display with size 1600x1200 and 16 bit color. Color can be changed to 24 or 8\n",
        "os.environ['DISPLAY']=':1.0'    # tell X clients to use our virtual DISPLAY :1.0"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Reading package lists... Done\n",
            "Building dependency tree       \n",
            "Reading state information... Done\n",
            "xvfb is already the newest version (2:1.19.6-1ubuntu4.9).\n",
            "0 upgraded, 0 newly installed, 0 to remove and 40 not upgraded.\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-HgVkzmSTnK3"
      },
      "source": [
        "# Import Module\n",
        "from tkinter import *\n",
        "\n",
        "from tkinter.filedialog import askopenfilename\n",
        "from PIL import Image,ImageTk\n",
        "\n",
        "import tabula\n",
        "def select_file():\n",
        "    global file_name\n",
        "    file_name = askopenfilename(initialdir = \"/\",title = \"Select File\")\n",
        "# PDF TO EXCEL\n",
        "def pdf_to_excel():\n",
        "    if file_name.endswith('.pdf, .csv, .pdf, .py'):\n",
        "        # Read PDF File\n",
        "        df = tabula.read_pdf(file_name, pages = 'all')[0]\n",
        "\n",
        "        # Convert into Excel File\n",
        "        df.to_excel('BdnatureExcel.xlsx', pages= 4, stream=True)\n",
        "\n",
        "# PDF TO CSV\n",
        "def pdf_to_csv():\n",
        "    if file_name.endswith('.pdf'):\n",
        "        # Read PDF File\n",
        "        # this contain a list\n",
        "        df = tabula.read_pdf(file_name, pages = 'all')[0]\n",
        "        # Convert into CSV File\n",
        "        df.to_csv('BdnatureCSV.csv', pages=4, stream=True)\n",
        "\n",
        "# Create Object\n",
        "root = Tk()\n",
        "# set Geometry\n",
        "root.geometry('400x540')\n",
        "\n",
        "\n",
        "# use image as background \n",
        "img=Image.open(\"/content/convincon.jpg\")#D:\\pythonProject\\Finnovus_Assinment\\convincon.jpg\n",
        "photo=ImageTk.PhotoImage(img)\n",
        "\n",
        "lab=Label(image=photo)\n",
        "lab.pack()\n",
        "\n",
        "\n",
        "# Add Labels and Buttons\n",
        "Label(root, text=\"PDF CONVERSION\", font=\"italic 15 bold\", bg=\"light goldenrod\").place(x=55, y=5)\n",
        "\n",
        "Button(root,text=\"Select PDF File\",font=14, command= select_file).place(x=150, y=310)\n",
        "\n",
        "\n",
        "excel_btn = Button(root,text=\"PDF to Excel\",relief=\"solid\",bg=\"white\",font=15, command=pdf_to_excel)\n",
        "excel_btn.place(x=100, y=380)\n",
        "\n",
        "csv_btn = Button(root,text=\"PDF to CSV\",relief=\"solid\",bg=\"white\",font=15, command = pdf_to_csv)\n",
        "csv_btn.place(x=250, y=380)\n",
        "\n",
        "\n",
        "\n",
        "# Execute Tkinter\n",
        "root.mainloop()"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}